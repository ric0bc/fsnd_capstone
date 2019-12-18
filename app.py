import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = True
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route("/movies")
    def get_movies():
        result = {
            'test': True
        }
        return jsonify(result)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()