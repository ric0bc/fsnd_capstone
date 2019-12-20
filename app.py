import os
from flask import Flask, jsonify, abort, request
from models import setup_db, Actor, Movie, Actor_Movie
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
        movies = list(map(Movie.format, Movie.query.all()))
        result = {
            'success': True,
            'movies': movies
        }
        return jsonify(result)
    
    @app.route("/movies/<int:movie_id>")
    def get_single_movie(movie_id):
        try:
            movie = Movie.query.get(movie_id)

            if movie is None:
                abort(404)
            
            return jsonify({
                'success': True,
                'movie': {
                    'id': movie.id,
                    'title': movie.title,
                    'release_date': movie.release_date
                }
            })
        except:
            abort(422)

    @app.route("/movies", methods=['POST'])
    def store_movies():
        body = request.get_json()

        try:
            new_title = body.get('title', None)
            new_release_date = body.get('release_date', None)
            new_actor = body.get('actor', None)
            
            movie = Movie(
                title = new_title,
                release_date = new_release_date
            )

            if new_actor:
                actor = Actor(
                    name = new_actor['name'],
                    age = new_actor['age'],
                    gender = new_actor['gender']
                )
                movie.actors.append(actor)
                

            movie.insert()

            return jsonify({
                'success': True,
                'message': 'New Movie stored'
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):

        try:
            movie = Movie.query.get(movie_id)

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'message': '{} Movie ID deleted'.format(movie_id)
            })
        except:
            abort(422)

    @app.route("/movies/<int:movie_id>", methods=['PATCH'])
    def update_movie(movie_id):
        body = request.get_json()

        try:
            movie = Movie.query.get(movie_id)
            if movie is None:
                abort(404)

            new_title = body.get('title', None)
            if new_title:
                movie.title = new_title

            new_release_date = body.get('release_date', None)
            if new_release_date:
                movie.release_date = new_release_date

            movie.update()

            return jsonify({
                'success': True,
                'message': '{} Movie ID updated'.format(movie_id)
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['POST'])
    def not_allowed(movie_id):
        abort(405)

    @app.route("/actors")
    def get_actors():
        actors = list(map(Actor.format, Actor.query.all()))
        result = {
            'success': True,
            'actors': actors
        }
        return jsonify(result)

    @app.route("/actors/<int:actor_id>")
    def get_single_actor(actor_id):
        try:
            actor = Actor.query.get(actor_id)

            if actor is None:
                abort(404)
            
            return jsonify({
                'success': True,
                'actor': {
                    'id': actor.id,
                    'name': actor.name,
                    'age': actor.age,
                    'gender': actor.gender
                }
            })
        except:
            abort(422)

    @app.route("/actors", methods=['POST'])
    def store_actor():
        body = request.get_json()
        
        try:
            new_name = body.get('name', None)
            new_age = body.get('age', None)
            new_gender = body.get('gender', None)
            new_movie = body.get('movie', None)

            actor = Actor(
                name = new_name,
                age = new_age,
                gender = new_gender
            )

            if new_movie:
                movie = Movie(
                    title = new_movie['title'],
                    release_date = new_movie['release_date']
                )
                actor.movies.append(movie)

            actor.insert()

            return jsonify({
                'success': True,
                'message': 'New Actor stored'
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):

        try:
            actor = Actor.query.get(actor_id)

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'message': '{} Actor ID deleted'.format(actor_id)
            })
        except:
            abort(422)

    @app.route("/actors/<int:actor_id>", methods=['PATCH'])
    def update_actor(actor_id):
        body = request.get_json()

        try:
            actor = Actor.query.get(actor_id)
            if actor is None:
                abort(404)

            new_name = body.get('name', None)
            if new_name:
                actor.name = new_name

            new_age = body.get('age', None)
            if new_age:
                actor.age = new_age
            
            new_gender = body.get('gender', None)
            if new_gender:
                actor.gender = new_gender

            actor.update()

            return jsonify({
                'success': True,
                'message': '{} Actor ID updated'.format(actor_id)
            })
        except:
            abort(422)

    '''
    Errors
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
        }), 422

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
        }), 405

    @app.errorhandler(500)
    def method_not_allowed(error):
        return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
        }), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run()