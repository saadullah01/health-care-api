'''
 This file will define and execute the main flow of our
 app. It will include all modules that will be created separately
 and will use their functionalities accordingly.
'''

from flask import Flask, request

from device_module.devices import device_api as d
from chat_module.chat import chat_api as c

app = Flask(__name__)

######################################################################################
################################## DEVICE API ########################################
######################################################################################
@app.route('/device', methods=['GET', 'POST'])
def device_handler():
    '''
        Handles the following 3 kinds of requests for device API:

        1. GET a specific patient's data for a specific device
        2. POST a specific patient's data for a specific device
        3. DELETE a specific patient's data for a specific device (TBD)
    '''
    request_type = {
        'GET': d.get_reading,
        'POST': d.add_reading
    }
    data = request.json
    response = request_type[data['request']](data)
    return response

######################################################################################
################################## CHAT API ########################################
######################################################################################
@app.route('/chat', methods=['GET', 'POST'])
def chat_handler():
    '''
        Handles the following 3 kinds of requests for chat API:

        1. GET a specific coversation for specific users
        2. POST a specific message to specific conversation
        3. POST to start a new conversation (TBD)
        4. DELETE a specific message from a coversation (TBD)
        5. DELETE a specific conversation (TBD)
    '''
    request_type = {
        'GET': c.get_reading,
        'POST': c.add_reading
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
