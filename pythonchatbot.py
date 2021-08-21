# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 15:23:00 2021

@author: user
"""

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('VQPPM3M18aTELHcjypTzeFoRx8Dq746iQnEkVegyJNJU')
assistant = AssistantV2(
        version='2021-06-14',
        authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')
response = assistant.create_session(
        assistant_id ='88142127-adb2-4c72-8091-6861b42428e5'
).get_result()
session_id = response
session_id = session_id["session_id"]
print(type(session_id))
print(session_id)

while True:
    input_text = input("enter the text")
            
    response = assistant.message(
        assistant_id = '88142127-adb2-4c72-8091-6861b42428e5',
        session_id=session_id,
        input={
            'message_type' : 'text',
            'text': input_text
         }
     ).get_result()
    print(response["output"]["generic"][0]["text"])
   
                    
            
