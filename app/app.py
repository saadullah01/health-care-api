'''
 This file will define and execute the main flow of our
 app. It will include all modules that will be created separately
 and will use their functionalities accordingly.
'''

from flask import Flask, request

from device_module.devices import device_api as d
from chat_module.chat import chat_api as c
from user_module.user import user_api as u

app = Flask(__name__)

# Device API
@app.route('/device', methods=['GET', 'POST'])
def device_handler():
    '''
        ########################################################
        #################### DEVICE API ########################
        ########################################################

        Handles the following 3 kinds of requests for device API:

        1. GET patient's data for a device
        2. PUT patient's data for a device
        3. DELETE patient's data for a device (TBD)
    '''
    request_type = {
        'GET': d.get,
        'PUT': d.put,
        'DELETE': d.delete
    }
    data = request.json
    response = request_type[data['request']](data)
    return response

# Chat API
@app.route('/chat', methods=['GET', 'POST'])
def chat_handler():
    '''
        ########################################################
        #################### CHAT API ##########################
        ########################################################

        Handles the following 5 kinds of requests for chat API:

        1. GET coversation for specific users
        2. PUT a message to a specific conversation
        3. PUT_C (conversation) to the database (TBD)
        4. DELETE_M (message) from a specific coversation (TBD)
        5. DELETE_C (conversation) to the database (TBD)
    '''
    request_type = {
        'GET': c.get,
        'PUT': c.put,
        'PUT_C': c.put_c,
        'DELETE_M': c.delete_m,
        'DELETE_C': c.delete_c
    }
    data = request.json
    response = request_type[data['request']](data)
    return response

# User API
@app.route('/user', methods=['GET', 'POST'])
def user_handler():
    '''
        ########################################################
        #################### USER API ##########################
        ########################################################

        Handles the following 5 kinds of requests for chat API:

        1. GET user data by 'email'
        2. PUT user to the database (check for existence of same user before through 'email')
        3. DELETE user by 'email'
        4. GET_P (patients) for a user (i.e. medical professional)
        5. GET_MP (medical professionals) for a user (i.e. patient)
    '''
    request_type = {
        'GET': u.get,
        'ADD': u.put,
        'DELETE': u.delete,
        'GET_P': u.get_p,
        'GET_MP': u.get_mp
    }
    data = request.json
    response = request_type[data['request']](data)
    return response

# Main Page
@app.route('/')
def index():
    return "<h1>Welcome to our Health Care App!!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
