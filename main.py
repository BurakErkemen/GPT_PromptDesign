"""
task,context,exemplar,persona,format,tone
important --------------------->optional
"""
#Kütüphaneler
import os
import time
from openai import OpenAI
import streamlit as slt

#İnput değerini alıyoruz
user_input=input('You: ')
#Prompt çıktısı veren prompt tasarımız
prompt = """
I want you to act as a ChatGPT prompt generator, I will send a topic, you have to generate a ChatGPT prompt based on the content of the topic, the prompt should start with "I want you to act as ", and guess what I might do, and expand the prompt accordingly Describe the content to make it useful.
"""
#client yapısıyla oluşturmadan hatalı sonuç döndürüyoruz.
client = OpenAI(
  openai_api_key = 'GPT-API-KEY'
)
while True:
    user_input = input('You: ')
    #Programı sonlandırmak için "exit" yazıyoruz.
    if user_input.lower() == 'exit':
        print('My Bot: Bye!')
        break

    # GPT-3.5-turbo apisi kullanıyoruz.
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        max_tokens=150,
        messages=[
            {"role": "system", "content": prompt}
            ,
            {"role": "user", "content": user_input}
  ]
)
    #Prompt çıktısını yazdırıyoruz.
    print(completion.choices[0].message.content)
