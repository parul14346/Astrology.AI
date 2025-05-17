import google.generativeai as genai
import os
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_1"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_analysis(prompt):
    if prompt is not None:
       st.markdown("Generating...")
    else:
        st.warning("Could not Generate...")
    response = model.generate_content(prompt)
    return (st.write(response.text))

