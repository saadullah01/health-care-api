'''
 This file contains functions for all the devices interface
 and add user entered data to the database in proper format.
'''

import os

def take_reading(user_ID, device_type, conn):
    cursor = conn.cursor()

    device_map = {
        1: "temperature (F)",
        2: "weight (lbs)",
        3: "BP (mmHg)",
        4: "pulse rate (BPM)",
        5: "oxygen level (SpO2)",
        6: "glucose level (mmol/L)",
        7: "height (inches)"
    }

    while True:
        try:
            reading = float(input('Enter the ' + device_map[device_type] + ": "))
            cursor.execute('''INSERT INTO measurements(user_ID,device_ID,value) VALUES(?,?,?);''', (user_ID, device_type, reading))
            conn.commit()
            print("Successfully entered!!!")
            break
        except:
            os.system('clear')
            print('Invalid input! Try again!!!\n')
