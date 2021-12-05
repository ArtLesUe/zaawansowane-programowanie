from flask_restful import Resource
import modules.database as database
from models.Rating import Rating


class ApiGetRatings(Resource):
    def get(self):
        return database.read_movies_from_database(Rating, 'database/ratings.csv')
