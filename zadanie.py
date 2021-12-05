from flask import Flask
from flask_restful import Resource, Api

from api.GetMovies import ApiGetMovies
from api.GetHelloApi import ApiGetHello
from api.GetTags import ApiGetTags
from api.GetRatings import ApiGetRatings
from api.GetLinks import ApiGetLinks


app = Flask(__name__)
api = Api(app)

api.add_resource(ApiGetHello, '/')
api.add_resource(ApiGetMovies, '/movies')
api.add_resource(ApiGetLinks, '/links')
api.add_resource(ApiGetRatings, '/ratings')
api.add_resource(ApiGetTags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
