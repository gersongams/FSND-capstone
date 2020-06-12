import os

basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN": "dev-b4fl3591.us.auth0.com",
    "ALGORITHMS": ["RS256"],
    "API_AUDIENCE": "anime"
}

tokens = {
    "user_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVITHZkRWsyeXJ0TWZsZzdpN1pTWCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iNGZsMzU5MS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlMzBmNDYwNWM1N2MwYmEyZGFmMjAyIiwiYXVkIjoiYW5pbWUiLCJpYXQiOjE1OTE5NDczNDIsImV4cCI6MTU5MjAzMzc0MiwiYXpwIjoieHdlUVd6TkVRakVRV3pSVEFLQWh5NWZjNVE1bzFlU3giLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphbmltZXMiXX0.hgHvB0azeq1c5ljaaqfvbhc2sLKbBAnDW6cNK19RUE-Z0-JWE4WnjValc2tFkn7DDb0uv5hZkIclLjLwAlBpF4xomz0mNsz1QTSY7qwt5j1fOQtZzSaKuxD9Mf3nP0ugeI_t9TOa-cvnbLybLnvnEjYZuFXXuXay1JIJPS_2zbVwfHOprOWvvPQdIWL4tkPCqbrQcyS_hCgqSoMHVi1c0MyKID3I3Sx_9nFja8D7uqH3nQg7N0QeHvD2GacgFx0ZMuhTad2GYWhseyrJOXxQgQiikxZ_iMd_NRpQujpZ0FK9jZr9Wvt2UWoIOaedEz3MvB3MZkEK_jXRL8898Iv3ug",
    "admin_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVITHZkRWsyeXJ0TWZsZzdpN1pTWCJ9.eyJpc3MiOiJodHRwczovL2Rldi1iNGZsMzU5MS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlMzBmNjcwNWM1N2MwYmEyZGFmMjA0IiwiYXVkIjoiYW5pbWUiLCJpYXQiOjE1OTE5NDcyNjksImV4cCI6MTU5MjAzMzY2OSwiYXpwIjoieHdlUVd6TkVRakVRV3pSVEFLQWh5NWZjNVE1bzFlU3giLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphbmltZXMiLCJnZXQ6YW5pbWVzIiwicGF0Y2g6YW5pbWVzIiwicG9zdDphbmltZXMiXX0.bSiEnqtAutuvt6bVrbftn44g6aOSUKUXfDWYw5godAOl8tXNcN7olf9v1WgpU1lsAyW8nwN36fEr5PttVRz7_k-HOtpMcT90ZRdm0_0LfvBc_Q99cOmEhTDcdu2x-t3s8FawbQn6z6vims_w5_skRoS7E1vGe8SzwpweM_oykoKZ2q7VoWSaUGPOAEnoETTgwF7DTeF_ky3T8H-KbW-I46lB_oXIZQ91L25BZIaJ0WtR7WvwqY9l2vK7gSfbEfAnhWAn5TX9zb175uD7WhF7CcR3ccxhBis5MWtdL3KsP2GhvJ17LfAFM2ZrAiWoCFhRKpJNIUvMaFY7NbNGTPeJgw",
}


def get_database_path():
    is_prod = os.environ.get('IS_HEROKU', None)
    database_path = ''

    if is_prod:
        database_path = "postgres://hlfqgnttcnktiz:da37928c7375f60206a5524585b7708d168e902561d993b10860a9e54a5cc3c4@ec2-34-202-88-122.compute-1.amazonaws.com:5432/d7bgv2q367s97t"
    else:
        database_name = "anime"
        database_user = "postgres"
        database_password = "docker"
        database_host = "localhost"
        database_port = "5432"
        database_path = "postgres://{}:{}@{}/{}".format(
        database_user, database_password, '{}:{}'.format(database_host, database_port), database_name)

    return database_path