import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import datetime

from app import create_app
from models import setup_db, Movie

class CapstoneTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9FRTRSamd5TWpOR1JURTFNMFE0TWtVNFFVWXpSRGsyTXpnek1EUTNRVGhETmtGRE5UVXdNUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdnh3b3YtMy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRmY2QxY2E0NDJkNGMwZWI5ZjY1MjNmIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTc2ODU0MTY1LCJleHAiOjE1NzY5NDA1NjUsImF6cCI6IkpRdlFoTXp3bUVTWEhGMnRid3dGeHF2Wk9OTjRBbFlHIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.KphT3pTSC7y5BmgpoZaw4y62LblchbgGRn1Wrg87eSOJuOnI2Fa6zKr6UkfXsWKjxBQSvn7PKAVRanxKSVfj3jmO3lyErr0uARYHrO5kMjVL5hugTIuWQ8O062szBA2OzCFjPSnHdnYc8JF84DdUz56iNxJafc1rXy2OoinWjqgfNX-jLnRaCXc_G9cfgVvwSyvGNYMAcej8OMwWkL9IHBYgGxSh87GvHYJHfnbB9t-_HtE-vYY4IKfAe09x5CniZIAQOKlbhXZeNSbsRGeIpBUMNasON4pH-MJZuROTPp3e-GYagHHSGUvfymd62qWmIknHMrofmCGuBAP-6uD-PA'}
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

    def test_get_movies(self):
        """Test _____________ """
        res = self.client().get('/movies', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        # self.assertTrue(data["movies"])
    
    def test_404_sent_requesting_false_endpoint(self):
        res = self.client().get('/mooviees')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], 'Not found')

    def test_post_movie(self):
        res = self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movie(self):
        self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        })
        res = self.client().get('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])
    
    def test_405_if_movie_creation_not_allowed(self):
        res = self.client().post('/movies/17', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'method not allowed')

    def test_delete_movie(self):
        self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        })
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_movie_with_false_id(self):
        res = self.client().delete('/movies/1321')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], 'unprocessable')
    
    def test_update_movie(self):
        self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        })
        res = self.client().patch('/movies/1', json={
            'title': 'Updated Movie',
            'release_date': datetime.datetime.now()
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_update_movie_with_false_id(self):
        res = self.client().patch('/movies/123', json={
            'title': 'Updated Movie',
            'release_date': datetime.datetime.now()
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], 'unprocessable')

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_actor(self):
        self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 59,
            'gender': 'woman'
        })
        res = self.client().get('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_post_actor(self):
        res = self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 30,
            'gender': 'man'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'New Actor stored')

    def test_post_actor_with_movie(self):
        res = self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 30,
            'gender': 'man',
            'movie': {
                'title': 'New testing Movie',
                'release_date': '2019-12-20 10:19:55'
            }
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'New Actor stored')

    def test_delete_actor(self):
        self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 30,
            'gender': 'man'
        })
        res = self.client().delete('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor(self):
        self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 30,
            'gender': 'man'
        })
        res = self.client().patch('/actors/1', json={
            'name': 'New Actor Updated',
            'age': 31,
            'gender': 'woman'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()