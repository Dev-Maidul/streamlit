from google import genai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key=os.environ.get("GEMNI_API_KEY")

client=genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Give me an idea of gemni api in 50 words",
)

st.markdown(response.text)