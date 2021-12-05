import json
from flask_restful import Resource
import modules.database as database


class ApiGetMovies(Resource):
    def get(self):
        return database.read_movies_from_database()
