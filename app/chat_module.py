'''
 This file contains functions for all the chat interface.
 It also adds user entered data to the database in proper format.
'''
import sqlite3

class chat_api():
    def __init__(self):
       self.db = 'app/health_care_DB.db'

    def get_reading(self, inp):
        connection = sqlite3.connect(self.db)
        conversation_ID = None
        response = {
            'success': False,
            'message': list()
        }
        # conversation_ID
        try:
            conversation_ID = int(inp['conversation_ID'])
        except:
            response['message'] = "Error! Invalid conversation_ID format"
            return response
        
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM messages WHERE conversation_ID==?;''', (conversation_ID,))
        readings = cursor.fetchall()
        connection.commit()
        connection.close()

        response['success'] = True
        for r in readings:
            response['message'].append("Sender = " + str(r[0]) + " Receiver = " + str(r[1]) + " Message = " + str(r[4]) + " Time = " + str(r[5]))
        
        return response

    def add_reading(self, inp):
        connection = sqlite3.connect(self.db)
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
