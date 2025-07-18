import streamlit as st
import openai

st.set_page_config(page_title="AI Career Advisor", page_icon="🤖")

st.title("🎓 AI Career Advisor")
st.write("Get personalized career advice using AI!")

openai.api_key = st.secrets["openai_api_key"]

user_input = st.text_input("Enter your interests, skills, or stream:")

if user_input:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a career counselor bot helping students choose a suitable career path."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response['choices'][0]['message']['content'])
