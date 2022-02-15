'''
    Test for devices modules
'''

import sqlite3
import os
from device_module import add_reading

def test_thermometer():
    connection = sqlite3.connect('test_DB.db')
    cursor = connection.cursor()

    # Creating "measurements" Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS measurements (
                    user_ID integer,
                    device_ID intger,
                    reading double,
                    time datetime
                );''')
    connection.commit()

    _ = add_reading({
        'user_ID': 1,
        'device_ID': 2,
        'reading': 98,
        'time': '2022-02-15 00:00:00',
        'db': connection
    })

    cursor.execute('''SELECT reading FROM measurements WHERE user_ID==1 AND device_ID==2;''')
    result = cursor.fetchone()
    connection.close()
    os.remove('test_DB.db')
    assert result[0] == 98.0
