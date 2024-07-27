import google.generativeai as genai
import textwrap
from IPython.display import display, Markdown
import os
from dotenv import load_dotenv

load_dotenv()

# Google Gemini API anahtarınızı buraya girin
GOOGLE_API_KEY = "Gemini_API_KEY"

# Google Gemini API'yi yapılandır
genai.configure(api_key=GOOGLE_API_KEY)

# Kullanılabilir modelleri listele
available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
print("Available models:")
for model_name in available_models:
    print(model_name)

# Gemini modelini seç ve oluştur
model_name = 'models/gemini-1.5-pro-latest'  # Kullanmak istediğiniz modeli seçin
model = genai.GenerativeModel(model_name)

# Kullanıcının konusu
topic = input("Ask Question: ")

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

# Soruyu modele ileterek yanıtı al
response = model.generate_content(prompt_with_topic)

# Yanıtın adaylarını göster
print("\nCandidates:")
for candidate in response.candidates:
    print(candidate.content.parts[0].text)
    print("-" * 80)

# Yanıt engellenmediyse Markdown formatında göster
if response.candidates:
    text_to_display = textwrap.indent(response.candidates[0].content.parts[0].text, '> ')
    display(Markdown(text_to_display))
else:
    print("Response was blocked.")
