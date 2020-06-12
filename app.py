from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from models import setup_db, Anime
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins.
    CORS(app)

    # Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # ROUTES

    # GET endpoint to obtain the all the animes
    @app.route('/animes', methods=['GET'])
    @requires_auth('get:animes')
    def get_animes(payload):
        animes = Anime.query.order_by(Anime.id).all()

        return jsonify({
            "success": True,
            "animes": [anime.format() for anime in animes]
        })

    # GET endpoint to obtain the detail of one anime
    @app.route('/animes/<int:anime_id>', methods=['GET'])
    @requires_auth('get:animes')
    def get_anime_detail(payload, anime_id):
        anime = Anime.query.filter_by(id=anime_id).one_or_none()
        if anime is None:
            abort(404)

        return jsonify({
            'success': True,
            'anime': anime.format()
        })

    # POST endpoint to create a new anime
    @app.route('/animes', methods=['POST'])
    @requires_auth('post:animes')
    def create_anime(payload):
        if request.data:
            body = request.get_json()
            title = body.get('title', None)
            image_url = body.get('image_url', None)
            mal_url = body.get('mal_url', None)
            score = body.get('score', None)
            rank = body.get('rank', None)

            if title is None:
                abort(422)

            anime = Anime(
                title=title,
                image_url=image_url,
                mal_url=mal_url,
                score=score,
                rank=rank
            )

            Anime.insert(anime)
            new_anime = Anime.query.filter_by(id=anime.id).first()

            return jsonify({
                'success': True,
                'anime': new_anime.format()
            })
        else:
            abort(422)

    # PATCH endpoint to update a anime by anime_id
    @app.route('/animes/<int:anime_id>', methods=['PATCH'])
    @requires_auth('patch:animes')
    def patch_anime(payload, anime_id):
        body = request.get_json()
        title = body.get('title', None)
        image_url = body.get('image_url', None)
        mal_url = body.get('mal_url', None)
        score = body.get('score', None)
        rank = body.get('rank', None)

        try:
            anime = Anime.query.filter_by(id=anime_id).one_or_none()
            if anime is None:
                abort(404)

            if title:
                anime.title = title
            if image_url:
                anime.image_url = image_url
            if mal_url:
                anime.mal_url = mal_url
            if score:
                anime.score = score
            if rank:
                anime.rank = rank

            anime.update()
            updated_anime = Anime.query.filter_by(id=anime_id).first()

            return jsonify({
                'success': True,
                'anime': updated_anime.format()
            })
        except:
            abort(422)

    # DELETE endpoint to delete the anime using the anime_id
    @app.route('/animes/<int:anime_id>', methods=['DELETE'])
    @requires_auth('delete:animes')
    def delete_animes(payload, anime_id):
        try:
            anime = Anime.query.filter_by(id=anime_id).one_or_none()
            if anime is None:
                abort(404)

            anime.delete()
            return jsonify({
                'success': True,
                'deleted': anime_id
            })
        except:
            abort(422)

    # # Error handlers for 400, 404, 422 and 500
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def error_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(422)
    def error_unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
