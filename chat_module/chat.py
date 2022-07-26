'''
 This file contains functions for all the chat interface.
 It also adds user entered data to the database in proper format.
'''
import sqlite3

class chat_api():
    def get(inp):
        connection = sqlite3.connect('database/health_care_DB.db')
        user_ID = None
        response = {
            'success': False,
            'message': list()
        }

        # user_ID
        try:
            user_ID = int(inp['user_ID'])
        except:
            response['message'] = "Error! Invalid user_ID format"
            return response
        
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM conversations WHERE user1_ID==? OR user2_ID==?;''', (user_ID, user_ID))
        readings = cursor.fetchall()

        response['success'] = True
        for r in readings:
            other_user_ID = int(r[1]) if user_ID != int(r[1]) else int(r[2])
            cursor.execute('''SELECT first_name, last_name, role_ID FROM users WHERE ID==?;''', (user_ID,))
            result = cursor.fetchone()
            
            response['message'].append({
                'conv_ID': int(r[0]),
                'user_ID': other_user_ID,
                'time': r[3],
                'first_name': result[0],
                'last_name': result[1],
                'role_ID': result[2]
            })
        connection.commit()
        connection.close()
        
        return response

    def put(inp):
        connection = sqlite3.connect('database/health_care_DB.db')
        sender_ID, receiver_ID, conversation_ID, message_type, message, time = None, None, None, None, None, None
        response = {
            'success': False,
            'message': None
        }
        # sender_ID
        try:
            sender_ID = int(inp['sender_ID'])
        except:
            response['message'] = "Error! Invalid sender_ID format"
            return response
        # receiver_ID
        try:
            receiver_ID = int(inp['receiver_ID'])
        except:
            response['message'] = "Error! Invalid receiver_ID format"
            return response
        # conversation_ID
        try:
            conversation_ID = float(inp['conversation_ID'])
        except:
            response['message'] = "Error! Invalid conversation_ID format"
            return response
        # message_type
        try:
            message_type = str(inp['message_type'])
        except:
            response['message'] = "Error! Invalid message_type format"
            return response
        # message
        try:
            message = str(inp['message'])
        except:
            response['message'] = "Error! Invalid message format"
            return response
        # time
        try:
            time = str(inp['time'])
        except:
            response['message'] = "Error! Invalid time format"
            return response

        cursor = connection.cursor()
        cursor.execute('''INSERT INTO messages(sender_ID,receiver_ID,conversation_ID,message_type,message,time) VALUES(?,?,?,?,?,?);''', (sender_ID, receiver_ID, conversation_ID, message_type, message, time))
        connection.commit()
        connection.close()

        response['success'] = True
        response['message'] = "Successfull!"
        return response

    def put_c(inp):
        pass

    def delete_m(inp):
        pass

    def delete_c(inp):
        pass
