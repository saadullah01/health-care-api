'''
 This file will define and execute the main flow of our
 app. It will include all modules that will be created separately
 and will use their functionalities accordingly.
'''

from flask import Flask, request
from flask_restful import Resource, Api

from device_module import add_reading, get_reading
# from device_module import add_reading

app = Flask(__name__)
api = Api(app)

class device_api(Resource):
    def get(self):
        data = request.json
        response = get_reading(data)
        return response

    def put(self):
        data = request.json
        response = add_reading(data)
        return response

api.add_resource(device_api, '/device_reading')

# def main():
#     # Creating New Database
#     response = add_reading({
#         'user_ID': 3,
#         'device_ID': 1,
#         'value': 98,
#         'time': '2022-02-15 00:00:00'
#     })
#     print(response)

if __name__ == '__main__':
    app.run(debug=True)
