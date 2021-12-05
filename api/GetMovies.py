from flask_restful import Resource
import modules.database as database
from models.Movie import Movie


class ApiGetMovies(Resource):
    def get(self):
        return database.read_movies_from_database(Movie, 'database/movies.csv')
