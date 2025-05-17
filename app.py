from dotenv import load_dotenv
load_dotenv() #Activate the Local Ens Vars

import streamlit as st
import google.generativeai as genai
import datetime

import geonamescache
from analysis import generate_analysis

# ...existing code...

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #b6e0fe 0%, #d6c1e6 60%, #f7bfcf 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #b6e0fe 0%, #d6c1e6 60%, #f7bfcf 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ...existing code...


## Create the front end and header

st.header(":blue[AstroVerse🔮:] Explore Your Stars with Intelligence", divider="violet")
st.subheader("Astrology Meets AI: Your Personalized Horoscope")



## Created Feature to select from the list of features
feature  = st.radio(
    "🧙‍♂️Select a feature:",
    [
        "🪐Birth Chart / Kundli Generation",
        "🧠 Personality Insights",
        "🚀 Career Path Predictions",
        "🤖 AI Chatbot for Astrology Q&A"
    ]
)

# User details input
st.markdown("#### :blue[Enter Your Birth Details]")
name = st.text_input("**Name**")
dob = st.date_input("**Date of Birth**", min_value = datetime.date(1900,1,1), max_value = datetime.date.today())
time_of_birth = st.time_input("**Time of Birth**")
## place_of_birth = st.text_input("**Place of Birth**", placeholder="City, Country") 

# Fetch Indian Cities using geonamescache
gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

# Filter cities where the country code is 'IN'
indian_cities = [city['name'] for city in cities.values() if city['countrycode'] == 'IN']
indian_cities = sorted(set(indian_cities))  # sort and remove duplicates

# Dropdown for Place of Birth with Indian cities
place_of_birth = st.selectbox("**Place of Birth**", options=indian_cities, index=0)

st.write(f"Hello, {name}! You were born in {place_of_birth} on {dob} at {time_of_birth}.")

question = " "

if feature == "AI Chatbot for Astrology Q&A":
    question = st.text_input("Ask your astrology-related question here")

button = st.button("Get AI Powered Insights")
if button:
    if feature == "Birth Chart / Kundli Generation":
        st.markdown("Generating your Birth Chart...")
         
        prompt=f"""Act as a Astrologer expert and Generate a detailed Vedic birth chart (Janam Kundli) based on the following details:
        Name: {name} 
        Date of Birth: {dob} 
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth}"""
        
        st.markdown(generate_analysis(prompt=prompt))
        st.success("✅ Birth Chart generated successfully!")
    
    elif feature == "Personality Insights":
        st.markdown("Analyzing your personality...")
        
        prompt=f"""Act as a Astrologer expert and Generate a detailed personality analysis based on the following details:
        Name: {name} 
        Date of Birth: {dob} 
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth}
        
        Details like Zodiac signs, Strengths, Weaknesses, and Personality Traits"""
        st.markdown(generate_analysis(prompt=prompt))
        st.success("✅ Personality insights generated successfully!")
    
    elif feature == "Career Path Predictions":
        st.markdown("Predicting your career path...")
        prompt=f"""Act as a Astrologer expert and Generate a detailed career path prediction based on the following details:
        Name: {name} 
        Date of Birth: {dob} 
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth} 
        
        Details like Career Options, Strengths, and Weaknesses, In what field you can excel, and what are 
        the best career options for you, expertise, and skills"""
        st.markdown(generate_analysis(prompt=prompt))
        st.success("✅ Career path predictions generated successfully!")
    
    elif feature == "AI Chatbot for Astrology Q&A":
        st.write("Generating your AI Chatbot for Astrology Q&A...")
        prompt=f"""Act as an expert Vedic astrologer. Answer the user's astrology-related question 
        based on the following birth details:

        Name: {name}  
        Date of Birth: {dob}  
        Time of Birth: {time_of_birth}  
        Place of Birth: {place_of_birth}
        Question: {question}"""
        st.markdown(generate_analysis(prompt=prompt))
        
        st.write("✅ Analysis Generated Successfully")
            
            
            
st.markdown("""
    <style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;
        background: white;color:blue;text-align: center;padding: 10px 0;
        z-index: 100;border-top: 1px solid #e6e6e6;}
    </style>
    <div class="footer">
        Made with ❤️ by Parul Nagar | Powered by Gemini + Streamlit
    </div>""",unsafe_allow_html=True
)




        
        