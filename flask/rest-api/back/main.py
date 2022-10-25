from flask import Flask
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)

# CORS(app, resources={r'특정라우터': {'origins': '특정도메인'}})
CORS(app, resources={r'*': {'origins': '*'}})

api = Api(app, version='1.0', title='Swagger Docs', description='Flask REST API Documentation', doc='/')

users = api.namespace('users', description='User Data API')
likes = api.namespace('likes', description='Likes Data API')

@users.route('')
class Users(Resource):
    def get(self):
        dummy_user_data = [
            {
                'id': 1,
                'name': 'june',
                'pwd': '1234',
            },
            {
                'id': 2,
                'name': 'dev',
                'pwd': '5678',
            },
        ]
        return dummy_user_data

@likes.route('')
class Likes(Resource):
    def get(self):
        dummy_user_data = [
            {
                'user_id': 1,
            },
        ]
        return dummy_user_data

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
