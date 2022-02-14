'''
    Test for devices modules
'''

import sqlite3
import os

def test_for_entering_data():
    connection = sqlite3.connect('test_DB.db')
    cursor = connection.cursor()

    # Creating "measurements" Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS measurements (
                    user_ID integer,
                    device_ID intger,
                    value double
                );''')
    connection.commit()
    cursor.execute('''INSERT INTO measurements(user_ID,device_ID,value) VALUES(1, 2, 99);''')
    connection.commit()
    cursor.execute('''SELECT value FROM measurements WHERE user_ID==1 AND device_ID==2;''')
    result = cursor.fetchone()
    connection.close()
    os.remove('test_DB.db')
    assert result[0] == 99.0
