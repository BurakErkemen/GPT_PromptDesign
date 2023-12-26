# Import the os package
import os
import time
from openai import OpenAI
# My first title is {user_input} (Give me prompt only)
user_input=input('You: ')
# prompt = """
# I want you to act as a prompt generator. 
# Firstly, I will give you a title like this: "You are an English Pronunciation Helper". 
# Then you give me a prompt like this: "I want you to act as an English pronunciation assistant for Turkish speaking people. I will write your sentences, and you will only answer their pronunciations, and nothing else. The replies must not be translations of my sentences but only pronunciations. Pronunciations should use Turkish Latin letters for phonetics. Do not write explanations on replies. 
# My first sentence is "how the weather is in Istanbul?"." (You should adapt the sample prompt according to the title I gave.The prompt should be self-explanatory and appropriate to the title, don't refer to the example I gave you.). 
# """

prompt = """
I want you to act as a ChatGPT prompt generator, I will send a topic, you have to generate a ChatGPT prompt based on the content of the topic, the prompt should start with "I want you to act as ", and guess what I might do, and expand the prompt accordingly Describe the content to make it useful.
"""


#openai.api_key = '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'
client = OpenAI(
  api_key='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'
  )
for _ in range(1):  # Örneğin, kez dönüyor
    time.sleep(10)

    if user_input == 'exit':
        print('My Bot: Bye!')
        break

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

    print(completion.choices[0].message.content)


"""
I want you to act as an ASP.NET developer. Your task is to provide a prompt related to ASP.NET development. The prompt should be clear and concise, focusing on a specific aspect or problem related to ASP.NET 
development. Avoid using technical jargon or complex concepts in the prompt. Remember to stop after providing a full description of the prompt.
"""

"""
I want you to act as a SQL tutor and guide me through the process of learning SQL. 
Start by explaining the basics of SQL, such as what it stands for and its purpose in database management. 
Then, provide an overview of the different components of SQL, including data manipulation, data definition, and data control. 
Additionally, share some practical examples and exercises to help me understand how to write SQL queries and perform common database operations.
"""
