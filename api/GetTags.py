from flask_restful import Resource
import modules.database as database
from models.Tag import Tag


class ApiGetTags(Resource):
    def get(self):
        return database.read_movies_from_database(Tag, 'database/tags.csv')
