import sqlite3

connection = sqlite3.connect('database/health_care_DB.db')
cursor = connection.cursor()

# Populating "roles" Table
roles = ['admin', 'doctor', 'nurse', 'patient', 'AI analyst', 'application developer', 'device integrator']
for r in roles:
    cursor.execute("INSERT INTO roles(Name) VALUES('" + r + "');")

# Populating "users" Table
users_sql = "INSERT INTO users(first_name,last_name,gender,contact_no,role_ID,dob,email,address,billing,allergies,medical_ID,family,medical_history,medical_condition,emergency_contact) "
cursor.execute(users_sql + '''VALUES('Osama','Prof','male','000000',1,'1999-08-09 00:00:00','osama@bu.edu','XXXXXX','same','none','XXXXXXX','none','none','none','none');''')
cursor.execute(users_sql + '''VALUES('Saad','Ullah','male','8573212741',2,'1999-08-09 00:00:00','saadu@bu.edu','1711 Comm Ave','same','none','XXXXXXX','none','none','none','none');''')
cursor.execute(users_sql + '''VALUES('Zaid','Tahir','male','000000',3,'1999-08-09 00:00:00','zaid@bu.edu','XXXXXX','same','none','XXXXXXX','none','none','none','none');''')
cursor.execute(users_sql + '''VALUES('Noor','Alina','female','000000',4,'1999-08-09 00:00:00','noor@gmail.com','XXXXXX','same','none','XXXXXXX','none','none','none','none');''')
cursor.execute(users_sql + '''VALUES('Jonah','Sameul','male','000000',4,'1999-08-09 00:00:00','jss12@bu.edu','XXXXXX','same','none','XXXXXXX','none','none','none','none');''')
cursor.execute(users_sql + '''VALUES('Mary','Cris','female','000000',3,'1999-08-09 00:00:00','mary@gmail.com','XXXXXX','same','none','XXXXXXX','none','none','none','none');''')
cursor.execute(users_sql + '''VALUES('Anni','India','male','000000',4,'1999-08-09 00:00:00','anni@gmail.com','XXXXXX','same','none','XXXXXXX','none','none','none','none');''')
cursor.execute(users_sql + '''VALUES('Cristina','Orla','female','000000',4,'1999-08-09 00:00:00','c@gmail.com','XXXXXX','same','none','XXXXXXX','none','none','none','none');''')

# Populating "treatments" Table
treatments_sql = "INSERT INTO treatments(mp_ID,p_ID) "
cursor.execute(treatments_sql + '''VALUES(2,4);''')
cursor.execute(treatments_sql + '''VALUES(2,5);''')
cursor.execute(treatments_sql + '''VALUES(2,7);''')
cursor.execute(treatments_sql + '''VALUES(2,8);''')
cursor.execute(treatments_sql + '''VALUES(3,4);''')
cursor.execute(treatments_sql + '''VALUES(3,5);''')
cursor.execute(treatments_sql + '''VALUES(3,7);''')
cursor.execute(treatments_sql + '''VALUES(6,7);''')
cursor.execute(treatments_sql + '''VALUES(6,8);''')

# Populating "devices" Table
devices_sql = "INSERT INTO devices(type,unit,date_of_purchase,MAC_address,user_ID,fw_version,sw_version) "
cursor.execute(devices_sql + '''VALUES('Thermometer','F','2020-09-11 00:00:00','xxxxx',2,'xxx','xxx');''')
cursor.execute(devices_sql + '''VALUES('Weight Scale','lbs','2020-09-11 00:00:00','xxxxx',2,'xxx','xxx');''')
cursor.execute(devices_sql + '''VALUES('Blood Pressure Monitor','mmHg','2020-09-11 00:00:00','xxxxx',2,'xxx','xxx');''')
cursor.execute(devices_sql + '''VALUES('Pulse Oximeter','BPM','2020-09-11 00:00:00','xxxxx',5,'xxx','xxx');''')
cursor.execute(devices_sql + '''VALUES('Oximeter','SpO2','2020-09-11 00:00:00','xxxxx',5,'xxx','xxx');''')
cursor.execute(devices_sql + '''VALUES('Glucometer','mmol/L','2020-09-11 00:00:00','xxxxx',5,'xxx','xxx');''')
cursor.execute(devices_sql + '''VALUES('Stadiometer','in','2020-09-11 00:00:00','xxxxx',5,'xxx','xxx');''')

# Populating "measurements" Table
measurements_sql = "INSERT INTO measurements(user_ID,device_ID,reading,time) "
cursor.execute(measurements_sql + '''VALUES(3,1,99,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(3,2,170,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(3,3,120,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(3,4,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(3,5,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(3,6,2,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(3,7,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(4,1,98,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(4,2,170,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(4,3,120,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(4,4,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(4,5,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(4,6,2,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(4,7,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(6,1,97,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(6,2,140,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(6,3,110,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(6,4,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(6,5,70,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(6,6,3,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(6,7,60,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(7,1,99,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(7,2,150,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(7,3,110,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(7,4,80,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(7,5,75,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(7,6,4,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(7,7,80,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(8,1,99,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(8,2,140,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(8,3,110,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(8,4,80,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(8,5,76,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(8,6,2,'2022-02-15 00:00:00');''')
cursor.execute(measurements_sql + '''VALUES(8,7,66,'2022-02-15 00:00:00');''')

# Populating "conversations" Table
conversations_sql = "INSERT INTO conversations(creator_ID,created_at) "
cursor.execute(conversations_sql + '''VALUES(1,'2022-02-15 00:00:00');''')
cursor.execute(conversations_sql + '''VALUES(3,'2022-02-15 00:00:00');''')
cursor.execute(conversations_sql + '''VALUES(4,'2022-02-15 00:00:00');''')
cursor.execute(conversations_sql + '''VALUES(5,'2022-02-15 00:00:00');''')

# Populating "messages" Table
messages_sql = "INSERT INTO messages(sender_ID,receiver_ID,conversation_ID,message_type,message,time) "
cursor.execute(messages_sql + '''VALUES(1,2,1,1,'Hello! I am 1.','2022-02-15 00:00:00');''')
cursor.execute(messages_sql + '''VALUES(2,1,1,1,'Hello 1! I am 2.','2022-02-15 00:00:00');''')
cursor.execute(messages_sql + '''VALUES(1,3,2,1,'Hello! Can you send me .txt file.','2022-02-15 00:00:00');''')
cursor.execute(messages_sql + '''VALUES(3,1,2,2,'/home/files/1.txt','2022-02-15 00:00:00');''')
cursor.execute(messages_sql + '''VALUES(1,4,3,1,'Hello! Can you send me .wav file.','2022-02-15 00:00:00');''')
cursor.execute(messages_sql + '''VALUES(4,1,3,3,'/home/files/1.wav','2022-02-15 00:00:00');''')
cursor.execute(messages_sql + '''VALUES(1,5,4,1,'Hello! Can you send me .mp4 file.','2022-02-15 00:00:00');''')
cursor.execute(messages_sql + '''VALUES(5,1,4,4,'/home/files/1.mp4','2022-02-15 00:00:00');''')

connection.commit()
connection.close()