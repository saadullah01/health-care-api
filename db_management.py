import sqlite3
import os

# Deleting Database (To create a fresh one)
os.remove('health_care_DB.db')

# Creating New Database
connection = sqlite3.connect('health_care_DB.db')
cursor = connection.cursor()

# Creating "roles" Table
cursor.execute('''CREATE TABLE IF NOT EXISTS roles (
                ID integer PRIMARY_KEY, 
                name text
            );''')

# Creating "users" Table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                ID integer PRIMARY_KEY, 
                first_name text,
                last_name text,
                gender text,
                contact_no integer,
                role_ID integer,
                dob datetime,
                address text,
                billing text,
                allergies text,
                medical_ID text,
                family text,
                medical_history text,
                medical_condition text,
                emergency_contact integer,
                FOREIGN KEY (role_ID) REFERENCES roles (ID)
            );''')

# Creating "devices" Table
cursor.execute('''CREATE TABLE IF NOT EXISTS devices (
                ID integer PRIMARY_KEY, 
                type text,
                unit text,
                date_of_purchase datetime,
                MAC_address text,
                user_ID integer,
                fw_version text,
                sw_version text,
                FOREIGN KEY (user_ID) REFERENCES users (ID)
            );''')

# Creating "measurements" Table
cursor.execute('''CREATE TABLE IF NOT EXISTS measurements (
                user_ID integer,
                device_ID intger,
                value double,
                FOREIGN KEY (user_ID) REFERENCES users (ID),
                FOREIGN KEY (device_ID) REFERENCES devices (ID)
            );''')

connection.commit()
connection.close()