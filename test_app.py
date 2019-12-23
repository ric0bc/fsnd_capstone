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
        self.auth_assistant = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9FRTRSamd5TWpOR1JURTFNMFE0TWtVNFFVWXpSRGsyTXpnek1EUTNRVGhETmtGRE5UVXdNUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdnh3b3YtMy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRmY2QxY2E0NDJkNGMwZWI5ZjY1MjNmIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTc3MDkzNDg2LCJleHAiOjE1Nzc5NTc0ODYsImF6cCI6IkpRdlFoTXp3bUVTWEhGMnRid3dGeHF2Wk9OTjRBbFlHIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmFjdG9ycyIsInJlYWQ6YWN0b3JzLWRldGFpbCIsInJlYWQ6bW92aWUtZGV0YWlsIiwicmVhZDptb3ZpZXMiXX0.jqvSzaicl6DtRPQJUH44V83JNSjxb0p3UR8JnelVtnQqV7PoG0Dml7oAR1DjZeX9ysWvNAMJcupnbgRBiBWNsyQYNToZ72BOPg2mAT5U3eWJHaYmxhZpQDud-eURdxx22jBDODLyWumQtN8fCLGt2RXq0YlY51pb57zsWhy1zWbGl54sYLfEn7jjwBM8roQtOinMbDljQ9fiqPL9QIf7sMQrOh_RaEP8hH0q4BCuArRO1FDYvybT2QkJ86b0afAwJsvChs7oIbLH-kuhDCBzuX1Uc5Q_VL5waYX7yxaaIU_Xin-TXQCMxHolmcbv6p0h_QROp8ypQ4dNS28cfeyrRQ'}
        self.auth_producer = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9FRTRSamd5TWpOR1JURTFNMFE0TWtVNFFVWXpSRGsyTXpnek1EUTNRVGhETmtGRE5UVXdNUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdnh3b3YtMy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRmY2ViMDE3ZjJkNDIwZWIwZGQ2ZjczIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTc3MDkyMjgxLCJleHAiOjE1Nzc5NTYyODEsImF6cCI6IkpRdlFoTXp3bUVTWEhGMnRid3dGeHF2Wk9OTjRBbFlHIiwiZ3R5IjoicGFzc3dvcmQiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6YWN0b3JzLWRldGFpbCIsInJlYWQ6bW92aWUtZGV0YWlsIiwicmVhZDptb3ZpZXMiXX0.U1pDR7fglfQXYisL26XQZBwLaR9YrNW3F0wC4BxhJbtjyy9ahcr5dbcln_IT4PcDxdEGpuQu1-7Cv3RlAiqGY-6V6hAOT6ZoqxgmHxt3fZhOaSOWiYaeqCu_uk3gycHUPRK9cqgxIBk5-E-_-WpB6O2zzVoQUEOcVOOUy8TgEYZFS_-PQX4k17h1zgf2o0ghEZoFVUoLIpBGoA9FZLFKQ2fimg0HCqqeNCdoUxnwKiKXPmvVSB7YzjHAmCjhmvbKO0w7fPvhdTKgq7F-vh6SvpJT2aVo0ojUC5kEC1Usk-dHCtiv1ZQNA5i8rVb96USbNOcD1_PXuQ5XcsV7kCAmSQ'}
        
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
        res = self.client().get('/movies', headers=self.auth_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        # self.assertTrue(data["movies"])
    
    def test_404_sent_requesting_false_endpoint(self):
        res = self.client().get('/mooviees', headers=self.auth_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], 'Not found')

    def test_post_movie(self):
        res = self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        }, headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movie(self):
        self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        }, headers=self.auth_producer)
        res = self.client().get('/movies/1', headers=self.auth_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])
    
    def test_405_if_movie_creation_not_allowed(self):
        res = self.client().post('/movies/17', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        }, headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'method not allowed')

    def test_delete_movie(self):
        self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        }, headers=self.auth_producer)
        res = self.client().delete('/movies/1', headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_movie_with_false_id(self):
        res = self.client().delete('/movies/1321', headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], 'unprocessable')
    
    def test_update_movie(self):
        self.client().post('/movies', json={
            'title': 'New Movie',
            'release_date': datetime.datetime.now()
        }, headers=self.auth_producer)
        res = self.client().patch('/movies/1', json={
            'title': 'Updated Movie',
            'release_date': datetime.datetime.now()
        }, headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_update_movie_with_false_id(self):
        res = self.client().patch('/movies/123', json={
            'title': 'Updated Movie',
            'release_date': datetime.datetime.now()
        }, headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], 'unprocessable')

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_actor(self):
        self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 59,
            'gender': 'woman'
        }, headers=self.auth_producer)
        res = self.client().get('/actors/1', headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_post_actor(self):
        res = self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 30,
            'gender': 'man'
        }, headers=self.auth_producer)
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
        }, headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'New Actor stored')

    def test_delete_actor(self):
        self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 30,
            'gender': 'man'
        }, headers=self.auth_producer)
        res = self.client().delete('/actors/1', headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor(self):
        self.client().post('/actors', json={
            'name': 'New Actor',
            'age': 30,
            'gender': 'man'
        }, headers=self.auth_producer)
        res = self.client().patch('/actors/1', json={
            'name': 'New Actor Updated',
            'age': 31,
            'gender': 'woman'
        }, headers=self.auth_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()