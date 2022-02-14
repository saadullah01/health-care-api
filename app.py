'''
 This file will define and execute the main flow of our
 app. It will include all modules that will be created separately
 and will use their functionalities accordingly.
'''

import sqlite3
import os
from devices import take_reading

def main():
    # Creating New Database
    connection = sqlite3.connect('health_care_DB.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT type FROM devices;''')
    device_list = cursor.fetchall()
    device_list = [i[0] for i in device_list]

    user_ID = int(input("Enter user ID: "))
    device_ID = None
    while True:
        for i in range(len(device_list)):
            print(i+1, device_list[i])
        device_ID = int(input("\nSelect the device to take the reading: "))
        if device_ID <= len(device_list):
            break
        os.system('clear')
    
    take_reading(user_ID, device_ID, connection)

    connection.close()

main()
