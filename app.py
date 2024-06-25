import streamlit as st
import openai
import pandas as pd
import json

# Load the healthcare data
with open('healthcare_data.json', 'r', encoding='utf-8') as f:
    healthcare_data = json.load(f)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(healthcare_data)

# Set up OpenAI API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_remedy(symptom):
    # Check if the symptom is in our dataset
    if symptom in df['symptom'].values:
        return df[df['symptom'] == symptom]['remedy'].values[0]
    else:
        # If not, use OpenAI to generate a response
        prompt = f"""
        You are a helpful healthcare assistant. Provide an immediate remedy for the given symptom. Be concise and clear.
        
        Symptom: {symptom}
        Remedy:
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides health advice. Only answer healthcare-related questions."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()

st.title("Healthcare Chatbot")

user_input = st.text_input("What symptom are you experiencing?")

if user_input:
    remedy = get_remedy(user_input.capitalize())
    if "remedy" in remedy.lower():
        st.write(f"Remedy for {user_input.capitalize()}:")
        st.write(remedy)
    else:
        st.write("Sorry, I can only provide information and remedies for healthcare-related symptoms. Please consult a healthcare professional for other inquiries.")

st.write("Note: This chatbot is for informational purposes only. Please consult a healthcare professional for medical advice.")
