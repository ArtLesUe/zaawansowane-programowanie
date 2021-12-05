from flask_restful import Resource
import modules.database as database
from models.Link import Link


class ApiGetLinks(Resource):
    def get(self):
        return database.read_movies_from_database(Link, 'database/links.csv')
