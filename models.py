from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

# database_path = os.environ['DATABASE_URL']
database_path = 'postgresql://ricky@localhost:5432/test'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


'''
Movie
Have title and release year
'''
class Movie(db.Model):  
  __tablename__ = 'Movie'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(DateTime)
  actors = db.relationship('Actor', secondary='Actor_Movie', backref='Movie', lazy='dynamic')

  def __init__(self, title, release_date, actors=""):
    self.title = title
    self.release_date = release_date
    self.actors = actors

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date
    }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit()

'''
Actor
Have name, age and gender
'''
class Actor(db.Model):  
  __tablename__ = 'Actor'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  movies = db.relationship('Movie', secondary='Actor_Movie', backref='Actor', lazy='dynamic')

  def __init__(self, name, age, gender, movies=""):
    self.name = name
    self.age = age
    self.gender = gender
    self.movies = movies

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit()

'''
Actor_Movie
Many-To-Many Relation
'''
Actor_Movie = db.Table('Actor_Movie',
  Column('actor_id', Integer, ForeignKey('Actor.id'), primary_key=True),
  Column('movie_id', Integer, ForeignKey('Movie.id'), primary_key=True)
)