from flask import Flask
from flask_restful import Resource, Api

from api.GetMovies import ApiGetMovies
from api.GetHelloApi import ApiGetHello


app = Flask(__name__)
api = Api(app)

api.add_resource(ApiGetHello, '/')
api.add_resource(ApiGetMovies, '/movies')

if __name__ == '__main__':
    app.run(debug=True)
