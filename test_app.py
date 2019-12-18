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
        res = self.client().get('/movies')
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

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()