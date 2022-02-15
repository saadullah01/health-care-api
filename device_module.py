'''
 This file contains functions for all the devices interface
 and add user entered data to the database in proper format.
'''

def add_reading(inp):
    user_ID, device_type, reading, time, conn = None, None, None, None, None
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
    # conn
    try:
        conn = inp['db']
    except:
        response['message'] = "Error! Invalid DB connection format"
        return response

    cursor = conn.cursor()
    cursor.execute('''INSERT INTO measurements(user_ID,device_ID,reading,time) VALUES(?,?,?,?);''', (user_ID, device_type, reading, time))
    conn.commit()

    response['message'] = "Successfull!"
    return response
