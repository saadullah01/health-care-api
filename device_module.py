'''
 This file contains functions for all the devices interface
 and add user entered data to the database in proper format.
'''
import sqlite3

def get_reading(inp):
    connection = sqlite3.connect('health_care_DB.db')
    user_ID, device_type = None, None
    response = {
        'success': False,
        'message': list()
    }
    # user_ID
    try:
        user_ID = int(inp['user_ID'])
    except:
        response['message'] = "Error! Invalid user_ID format"
        return response
    # device_ID
    try:
        device_type = int(inp['device_ID'])
    except:
        response['message'] = "Error! Invalid device_ID format"
        return response
    
    cursor = connection.cursor()
    cursor.execute('''SELECT reading, time FROM measurements WHERE user_ID==? AND device_ID==?;''', (user_ID, device_type))
    readings = cursor.fetchall()
    connection.commit()
    connection.close()

    response['success'] = True
    for r in readings:
        response['message'].append("Reading = " + str(r[0]) + " Time = " + str(r[1]))
    
    return response

def add_reading(inp):
    connection = sqlite3.connect('health_care_DB.db')
    user_ID, device_type, reading, time = None, None, None, None
    response = {
        'success': False,
        'message': None
    }
    # user_ID
    try:
        user_ID = int(inp['user_ID'])
    except:
        response['message'] = "Error! Invalid user_ID format"
        return response
    # device_ID
    try:
        device_type = int(inp['device_ID'])
    except:
        response['message'] = "Error! Invalid device_ID format"
        return response
    # value
    try:
        reading = float(inp['reading'])
    except:
        response['message'] = "Error! Invalid reading format"
        return response
    # time
    try:
        time = str(inp['time'])
    except:
        response['message'] = "Error! Invalid time format"
        return response

    cursor = connection.cursor()
    cursor.execute('''INSERT INTO measurements(user_ID,device_ID,reading,time) VALUES(?,?,?,?);''', (user_ID, device_type, reading, time))
    connection.commit()
    connection.close()

    response['success'] = True
    response['message'] = "Successfull!"
    return response
