import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Anime
from config import tokens


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "anime"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'docker', 'localhost:5432', self.database_name)
        self.admin_token = tokens['admin_token']
        self.user_token = tokens['user_token']

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.admin_token)
        }

        self.headers_user = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.user_token)
        }

        self.new_anime = {
            "title": "test_anime_title",
            "image_url": "test_image_url",
            "mal_url": "test_mal_url",
            "score": 10,
            "rank": 666
        }

        self.bad_anime = {
            "image_url": "test_image_url",
            "mal_url": "test_mal_url",
            "score": 10,
            "rank": 666
        }

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Test to get all the animes as ADMIN ROLE
    def test_get_all_animes(self):
        response = self.client().get('/animes', headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertGreaterEqual(len(data['animes']), 0)

    # Test to create a new animes as ADMIN ROLE
    def test_create_new_anime(self):
        response = self.client().post('/animes', json=self.new_anime, headers=self.headers)
        data = json.loads(response.data)
        anime = Anime.query.filter_by(id=data['anime']['id']).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(anime)

    # Test to create a new animes with missing title
    def test_fail_create_new_anime(self):
        response = self.client().post('/animes', json=self.bad_anime, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)

    # Test to create a new anime with the USER ROLE
    def test_fail_role_create_new_anime(self):
        response = self.client().post('/animes', json=self.new_anime, headers=self.headers_user)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    # Test to get an anime by id
    def test_get_anime_by_id(self):
        anime = Anime.query.first()
        response = self.client().get('/animes/{}'.format(anime.id), headers=self.headers)
        data = json.loads(response.data)
        anime_exists = Anime.query.filter_by(id=anime.id).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(anime_exists)

    # Test to get an anime by id that not exists
    def test_get_anime_by_id_not_exists(self):
        response = self.client().get('/animes/{}'.format(666), headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    # Test to update an anime by id
    def test_update_anime(self):
        anime = Anime.query.first()
        response = self.client().patch('/animes/{}'.format(anime.id), json={'title': 'new_title'}, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # Test to update an anime by id that not exists
    def test_update_fail_anime(self):
        response = self.client().patch('/animes/{}'.format(666), json={'title': 'new_title'}, headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)

    # Test to update an anime by id with USER ROLE
    def test_update_fail_role_anime(self):
        anime = Anime.query.first()
        response = self.client().patch('/animes/{}'.format(anime.id), json={'title': 'new_title'}, headers=self.headers_user)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    # Test to delete an anime by id
    def test_delete_anime(self):
        anime = Anime.query.first()
        response = self.client().delete('/animes/{}'.format(anime.id), headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # Test to delete an anime by id that not exists
    def test_delete_fail_anime(self):
        response = self.client().delete('/animes/{}'.format(666), headers=self.headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)

    # Test to delete an anime by id with the USER ROLE
    def test_delete_fail_role_anime(self):
        anime = Anime.query.first()
        response = self.client().delete('/animes/{}'.format(anime.id), headers=self.headers_user)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
