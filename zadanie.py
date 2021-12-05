from flask import Flask
from flask_restful import Resource, Api

from api.GetMovies import ApiGetMovies


app = Flask(__name__)
api = Api(app)


api.add_resource(ApiGetMovies, '/')

if __name__ == '__main__':
    app.run(debug=True)
