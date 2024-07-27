import google.generativeai as genai
import streamlit as st

API_KEY="AIzaSyC4D2fa6J7dPiF06yA8N2oeZYNECLCMJD0"

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = """
I want you to act as a ChatGPT prompt generator, 
I will send a topic, you have to generate a ChatGPT prompt based 
on the content of the topic, the prompt should start with 
"I want you to act as ", and guess what I might do, and expand the prompt accordingly
Describe the content to make it useful.
"""
while(True):
    question = input("User: ")
    
    if(question.strip() == ''):
        break

    response = chat.send_message(question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')

