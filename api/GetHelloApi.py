from flask_restful import Resource


class ApiGetHello(Resource):
    def get(self):
        return { 'status' : 'Hello Api' }
