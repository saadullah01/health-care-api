'''
 This file contains functions for all the devices interface
 and add user entered data to the database in proper format.
'''

def add_reading(inp):
    user_ID, device_type, reading, time, conn = None, None, None, None, None
    # user_ID
    try:
        user_ID = int(inp['user_ID'])
    except:
        return "Error! Invalid user_ID format"
    # device_ID
    try:
        device_type = int(inp['device_ID'])
    except:
        return "Error! Invalid device_ID format"
    # value
    try:
        reading = float(inp['reading'])
    except:
        return "Error! Invalid value format"
    # time
    try:
        time = str(inp['time'])
    except:
        return "Error! Invalid time format"
    # conn
    try:
        conn = inp['db']
    except:
        return "Error! Invalid DB format"

    cursor = conn.cursor()
    cursor.execute('''INSERT INTO measurements(user_ID,device_ID,reading,time) VALUES(?,?,?,?);''', (user_ID, device_type, reading, time))
    conn.commit()

    return "Successfull!"
