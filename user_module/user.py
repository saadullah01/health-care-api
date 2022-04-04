'''
 This file contains functions for all of the user interface.
'''
import sqlite3

class user_api():
    def get(inp):
        connection = sqlite3.connect('database/health_care_DB.db')
        email = None

        response = {
            'success': False,
            'message': None
        }

        # email
        try:
            email = str(inp['email'])
        except:
            response['message'] = "Error! Invalid email format"
            return response
        
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM users WHERE email==?;''', (email,))
        readings = cursor.fetchone()
        connection.commit()
        connection.close()

        response['success'] = True
        response['message'] = {
            'first_name': readings[1],
            'last_name': readings[2],
            'gender': readings[3],
            'contact_no': readings[4],
            'role_ID': readings[5],
            'dob': readings[6],
            'email': readings[7],
            'address': readings[8],
            'billing': readings[9],
            'allergies': readings[10],
            'medical_ID': readings[11],
            'family': readings[12],
            'medical_history': readings[13],
            'medical_condition': readings[14],
            'emergency_contact': readings[15]
        }
        return response

    def put(inp):
        connection = sqlite3.connect('database/health_care_DB.db')
        first_name, last_name, gender, contact_no, role_ID = None, None, None, None, None
        dob, email, address, billing, allergies = None, None, None, None, None
        medical_ID, family, medical_history, medical_condition, emergency_contact = None, None, None, None, None

        response = {
            'success': False,
            'message': None
        }

        # first_name
        try:
            first_name = str(inp['first_name'])
        except:
            response['message'] = "Error! Invalid first_name format"
            return response
        
        # last_name
        try:
            last_name = str(inp['last_name'])
        except:
            response['message'] = "Error! Invalid last_name format"
            return response

        # gender
        try:
            gender = str(inp['gender'])
        except:
            response['message'] = "Error! Invalid gender format"
            return response

        # contact_no
        try:
            contact_no = str(inp['contact_no'])
        except:
            response['message'] = "Error! Invalid contact_no format"
            return response
        
        # role_ID
        try:
            role_ID = int(inp['role_ID'])
        except:
            response['message'] = "Error! Invalid role_ID format"
            return response

        # dob
        try:
            dob = str(inp['dob'])
        except:
            response['message'] = "Error! Invalid dob format"
            return response

        # email
        try:
            email = str(inp['email'])
        except:
            response['message'] = "Error! Invalid email format"
            return response

        # address
        try:
            address = str(inp['address'])
        except:
            response['message'] = "Error! Invalid address format"
            return response

        # billing
        try:
            billing = str(inp['billing'])
        except:
            response['message'] = "Error! Invalid billing format"
            return response

        # allergies
        try:
            allergies = str(inp['allergies'])
        except:
            response['message'] = "Error! Invalid allergies format"
            return response

        # medical_ID
        try:
            medical_ID = str(inp['medical_ID'])
        except:
            response['message'] = "Error! Invalid medical_ID format"
            return response

        # family
        try:
            family = str(inp['family'])
        except:
            response['message'] = "Error! Invalid family format"
            return response

        # medical_history
        try:
            medical_history = str(inp['medical_history'])
        except:
            response['message'] = "Error! Invalid medical_history format"
            return response

        # medical_condition
        try:
            medical_condition = str(inp['medical_condition'])
        except:
            response['message'] = "Error! Invalid medical_condition format"
            return response

        # emergency_contact
        try:
            emergency_contact = str(inp['emergency_contact'])
        except:
            response['message'] = "Error! Invalid emergency_contact format"
            return response

        cursor = connection.cursor()
        users_sql = "INSERT INTO users(first_name,last_name,gender,contact_no,role_ID,dob,email,address,billing,allergies,medical_ID,family,medical_history,medical_condition,emergency_contact) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(users_sql, (first_name, last_name, gender, contact_no, role_ID, dob, email, address, billing, allergies, medical_ID, family, medical_history, medical_condition, emergency_contact))
        connection.commit()
        connection.close()

        response['success'] = True
        response['message'] = "Successfull!"
        return response

    def delete(inp):
        pass

    def get_p(inp):
        pass

    def get_mp(inp):
        pass

# inp = {
#     'first_name': 'Molly',
#     'last_name': 'Hicks',
#     'gender': 'bisexual',
#     'contact_no': '0000000000',
#     'role_ID': 3,
#     'dob': '2001-03-06 00:00:00',
#     'email': 'molly@gmail.com',
#     'address': '66 Beach Point Place',
#     'billing': 'same',
#     'allergies': 'none',
#     'medical_ID': 'XXXXXXXXX',
#     'family': 'none',
#     'medical_history': 'none',
#     'medical_condition': 'none',
#     'emergency_contact': 'XXXXXXXXXXX'
# }

# print(user_api.put(inp))