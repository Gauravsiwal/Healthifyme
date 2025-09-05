import os
import google.generativeai as genai
import pandas as pd
import streamlit as st

# Configure the model
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash-lite")


st.title('HEALTHIFY ME - :blue[YOUR PERSONEL HEALTH COACH]')
st.header('This application can guide you to keep yourself healthy. You can ask question related to your health any time')

# Create side bar to calculate BMI
st.sidebar.header('CALCULATE YOUR BMI')
height = weight = bmi = None
height = st.sidebar.text_input('Enter your height in meters: ')
weight = st.sidebar.text_input('Enter your weight in Kgs: ')
bmi = pd.to_numeric(weight)/pd.to_numeric(height)**2
st.sidebar.text(f'Your BMI: {round(bmi,2)} Kg/m^2')

# Generate the output from GenIA model
user_input= st.text_input('Ask your question here: ')
prompt = f'''Consider yourself as a health expert. You need to answer the question
asked by the user and guide him in order to imrpove his/her health. User has provided
the basic information like height is {height} meters, weight is {weight} kgs and BMI is
{bmi}. Use this information to give the cutomized solution (incase this data is none then ignore 
it). You result should be deivided in proper sections like problem, possible reason,
and solutions. Keep result summarized and in bulet points. Here is the question from user: {user_input}'''

if user_input:
    response = model.generate_content(prompt)
    st.write(response.text)







