import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Career Advisor", page_icon="🎓")
st.title("🎓 AI Career Advisor")
st.write("Get personalized career advice using AI!")

# Load API key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai_api_key"])

# User input
user_input = st.text_input("Enter your interests, skills, or stream:")

# If input is entered
if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a career counselor bot helping students choose a suitable career path."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response.choices[0].message.content)