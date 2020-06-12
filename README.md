# FSDN capstone project
This is the last project of the `Udacity-Full-Stack-Nanodegree` Course.

## Motivation
The motivation for this project is to create an API for a game that I'm planning to do in the next weeks. This project brings together everything I have learned during these months.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
$ virtualenv env
$ source env/bin/activate
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [auth0](auth0.com/) is a service to manage the authentication.


## Setting up the database
This project uses the heroku database instance, to use a local version, install Docker and in the terminal run:

```bash
# Pull the image of postgres
docker pull postgres

# Create a directory to store the data
mkdir -p $HOME/docker/volumes/postgres

# Run the container with the image previously downloaded
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application.

## API Reference
Getting Started
* Backend Base URL:
  * local: `http://127.0.0.1:5000/
  * heroku: `https://fsnd-capstone-anime.herokuapp.com`

### Existing Roles

They are 2 Roles with distinct permission sets:

1. User role:
  - GET /animes (get:animes): Can see all animes
2. Admin role (everything from User role plus)
  - POST /animes (post:animes): Can create new animes
  - DELETE /animes (delete:animes): Can remove existing animes from database
  - PATCH /animes (patch:animes): Can edit existing animes

### Authentication

* Authentication: To retrieve a new token for authorization use these emails and passoword:
  * admin_user: admin@test.com"
  * normal_user: user@test.com"
  * password: 123581321Udacity

```
https://dev-b4fl3591.us.auth0.com/authorize?
  audience=anime&
  response_type=token&
  client_id=xweQWzNEQjEQWzRTAKAhy5fc5Q5o1eSx&
  redirect_uri=http://localhost:5000/login-results
```
* Previous tokens are in the config file.

### Error handling
Errors are returned in the following json format:

```JSON
{
    "success": "False",
    "error": 422,
    "message": "Unprocessable entity",
}
```
The error codes currently returned are:

* 400 – bad request
* 404 – resource not found
* 422 – unprocessable
* 500 – internal server error

### Endpoints

* For testing reasons you can use this token (ADMIN PRIVILEGE):
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVITHZkRWsyeXJ0TWZsZzdpN1pTWCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iNGZsMzU5MS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlMzBmNjcwNWM1N2MwYmEyZGFmMjA0IiwiYXVkIjoiYW5pbWUiLCJpYXQiOjE1OTE5NDcyNjksImV4cCI6MTU5MjAzMzY2OSwiYXpwIjoieHdlUVd6TkVRakVRV3pSVEFLQWh5NWZjNVE1bzFlU3giLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphbmltZXMiLCJnZXQ6YW5pbWVzIiwicGF0Y2g6YW5pbWVzIiwicG9zdDphbmltZXMiXX0.bSiEnqtAutuvt6bVrbftn44g6aOSUKUXfDWYw5godAOl8tXNcN7olf9v1WgpU1lsAyW8nwN36fEr5PttVRz7_k-HOtpMcT90ZRdm0_0LfvBc_Q99cOmEhTDcdu2x-t3s8FawbQn6z6vims_w5_skRoS7E1vGe8SzwpweM_oykoKZ2q7VoWSaUGPOAEnoETTgwF7DTeF_ky3T8H-KbW-I46lB_oXIZQ91L25BZIaJ0WtR7WvwqY9l2vK7gSfbEfAnhWAn5TX9zb175uD7WhF7CcR3ccxhBis5MWtdL3KsP2GhvJ17LfAFM2ZrAiWoCFhRKpJNIUvMaFY7NbNGTPeJgw
```

* Replace the `<TOKEN>` word in the curl expressions for the token above to get results:

#### GET `/animes`
* Fetches all the animes and retrieve a list of dict in which the keys are the ids and the value is the corresponding string of the animes.
* Requires permission: `get:animes`
* Returns: An object with these keys:
    * `animes`: A list of animes objects, paginated (10) with the structure:
        * `image_url`: string,
        * `mal_url`: string,
        * `score`: float,
        * `rank`: number,
        * `id`: number,
        * `title`: string
    * `success`: The success flag

```bash
curl -X GET 'https://fsnd-capstone-anime.herokuapp.com/animes' \
--header 'Authorization: Bearer <TOKEN>'
```

```JSON
{
  "animes": [
    {
      "id": 2,
      "image_url": "https://myanimelist.net/anime/21/One_Piece",
      "mal_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
      "rank": 666,
      "score": 10.0,
      "title": "after_patch_1"
    }
  ],
  "success": true
}
```

### GET `/animes/:anime_id/`
* Get anime using a `anime_id` parameter
* Requires permission: `get:animes`
* Request arguments:
    * `anime_id` (number): The anime id
* Returns: An object with theses keys:
    * `anime` A JSON with the anime information
    * `success` The success flag

```bash
curl -X POST 'https://fsnd-capstone-anime.herokuapp.com/animes/1' \
--header 'Authorization: Bearer <TOKEN>'
```

```JSON
{
  "anime": {
    "id": 2,
    "image_url": "https://myanimelist.net/anime/21/One_Piece",
    "mal_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
    "rank": 666,
    "score": 10.0,
    "title": "after_patch_1"
  },
  "success": true
}
```

### DELETE `/animes/:anime_id/`
* Delete anime using a `anime_id` parameter
* Requires permission: `delete:animes`
* Request arguments:
    * `anime_id` (number): The anime id
* Returns: An object with theses keys:
    * `deleted` The ID of the anime deleted.
    * `success` The success flag

```bash
curl -X DELETE 'https://fsnd-capstone-anime.herokuapp.com/animes/2' \
--header 'Authorization: Bearer <TOKEN>'
```

```JSON
{
  "deleted": 1,
  "success": true
}
```

### POST `/animes`
* Create a new anime.
* Requires permission: `post:animes`
* Request arguments:
  * `image_url`: string,
  * `mal_url`: string,
  * `score`: float,
  * `rank`: number,
  * `title`: string


* Returns: An object with theses keys:
    * `anime` Contains the ID of the anime created.
    * `success` The success flag

```bash
curl -X POST 'https://fsnd-capstone-anime.herokuapp.com/animes' \
--header 'Authorization: Bearer <TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Naruto",
    "image_url": "https://myanimelist.net/anime/21/One_Piece",
    "mal_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
    "score": 10,
    "rank": 666
}'
```

```JSON
{
  "anime": {
    "id": 4,
    "image_url": "https://myanimelist.net/anime/21/One_Piece",
    "mal_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
    "rank": 666,
    "score": 10.0,
    "title": "Naruto"
  },
  "success": true
}
```


### PATCH `/animes/:anime_id/`
* Update an anime using a `anime_id` parameter
* Requires permission: `patch:animes`
* Request arguments:
  * `image_url`: string,
  * `mal_url`: string,
  * `score`: float,
  * `rank`: number,
  * `title`: string


* Returns: An object with theses keys:
    * `anime` Contains the ID of the anime updated.
    * `success` The success flag

```bash
curl -X PATCH 'https://fsnd-capstone-anime.herokuapp.com/animes/4' \
--header 'Authorization: Bearer <TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Naruto"
}'
```

```JSON
{
  "anime": {
    "id": 4,
    "image_url": "https://myanimelist.net/anime/21/One_Piece",
    "mal_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
    "rank": 666,
    "score": 10.0,
    "title": "Naruto"
  },
  "success": true
}
```



## Testing
To run the tests, run
```
python test_flaskr.py
```

## Authors

* Gerson Garrido worked on the API and tests.
* Udacity provided the starter files for the project