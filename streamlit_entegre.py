import streamlit as st
from openai import OpenAI

# OpenAI API key
openai_api_key = 'API-kEY'

# OpenAI client
openai = OpenAI(api_key=openai_api_key)

# Prompt tasarımı
prompt = """
I want you to act as a ChatGPT prompt generator, 
I will send a topic, you have to generate a ChatGPT prompt based 
on the content of the topic, the prompt should start with 
"I want you to act as ", and guess what I might do, and expand the prompt accordingly
Describe the content to make it useful.
"""

# Streamlit uygulaması
st.markdown("## GPT Prompt Generator")

# Kullanıcının girişini al
user_input = st.text_input("You:")

# GPT-3 API'sini kullanarak yanıt al
if st.button("Generate Response"):
    if user_input.lower() == 'exit':
        st.text('My Bot: Bye!')
    else:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.1,
            max_tokens=150,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
            ]
        )
        st.write('Abuzer Kömürcü: ' + completion.choices[0].message.content)
