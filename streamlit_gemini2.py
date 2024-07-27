import streamlit as st
import google.generativeai as genai
import textwrap
from IPython.display import display, Markdown

# Google Gemini API anahtarınızı buraya girin
GOOGLE_API_KEY = "AIzaSyC4D2fa6J7dPiF06yA8N2oeZYNECLCMJD0"

# Google Gemini API'yi yapılandır
genai.configure(api_key=GOOGLE_API_KEY)

# Kullanılabilir modelleri listele
available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

# Gemini modelini seç ve oluştur
model_name = 'models/gemini-1.5-pro-latest'  # Kullanmak istediğiniz modeli seçin
model = genai.GenerativeModel(model_name)

# Streamlit uygulaması
st.title("Gemini Prompt Generator")

# Kullanıcıdan konuyu al
topic = st.text_input("Enter a topic:", "Artificial intelligence and ethics")

# Prompt tasarımı
prompt = """
I want you to act as a ChatGPT prompt generator, 
I will send a topic, you have to generate a ChatGPT prompt based 
on the content of the topic, the prompt should start with 
"I want you to act as ", and guess what I might do, and expand the prompt accordingly
Describe the content to make it useful.
"""

# Prompt ile birleştirilen kullanıcının konusu
prompt_with_topic = prompt + f"How about \"{topic}\"?"

# Yanıtı gösterme işlemi
if st.button("Generate Prompt"):
    # Soruyu modele ileterek yanıtı al
    response = model.generate_content(prompt_with_topic)

    # Yanıtın adaylarını göster
    st.markdown("### Generated Prompt:")
    for candidate in response.candidates:
        st.write(candidate.content.parts[0].text)
