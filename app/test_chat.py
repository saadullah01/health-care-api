'''
    Test for chat modules
'''

import sqlite3
import chat_module as c

def test_add_reading():
    response = c.add_reading({
        'sender_ID': 1,
        'receiver_ID': 2,
        'conversation_ID': 1,
        'message_type': 1,
        'message': "Nice to meet you!",
        'time': "2022-02-15 00:00:00",
    })
    assert response['success'] == True

def test_get_reading():
    response = c.get_reading({
        'conversation_ID': 1
    })
    # Deleting test dummy entry
    connection = sqlite3.connect('app/health_care_DB.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM messages WHERE conversation_ID==1 AND message=='Nice to meet you!';''')
    connection.commit()
    connection.close()
    assert response['success'] = True
