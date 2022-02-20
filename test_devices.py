'''
    Test for devices modules
'''

import sqlite3
from device_module import add_reading, get_reading

def test_add_reading():
    response = add_reading({
        'user_ID': 1,
        'device_ID': 2,
        'reading': 98,
        'time': '2022-02-15 00:00:00'
    })
    assert response['success'] == True

def test_get_reading():
    response = get_reading({
        'user_ID': 1,
        'device_ID': 2
    })
    # Deleting test dummy entry
    connection = sqlite3.connect('health_care_DB.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM measurements WHERE user_ID==1 AND device_ID==2;''')
    connection.commit()
    connection.close()
    assert response['message'][0] == "Reading = 98.0 Time = 2022-02-15 00:00:00"
