'''
 This file will define and execute the main flow of our
 app. It will include all modules that will be created separately
 and will use their functionalities accordingly.
'''

import sqlite3
from device_module import add_reading

def main():
    # Creating New Database
    connection = sqlite3.connect('health_care_DB.db')
    
    response = add_reading({
        'user_ID': 3,
        'device_ID': 1,
        'value': 98,
        'time': '2022-02-15 00:00:00',
        'db': connection
    })
    print(response)

    connection.close()

main()
