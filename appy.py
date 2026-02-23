import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Bodo AI Assistant", layout="centered")

# Sidebar for Login
st.sidebar.title("🔐 Admin Access")
user_email = st.sidebar.text_input("Enter your email to unlock:")

# API Key and Admin Check
if user_email == "dhoneboro59@gmail.com":
    st.sidebar.success("Access Granted!")
    
    # Gemini Setup
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # AI System Instructions for Bodo
    instruction = "You are Gemini, but you must strictly speak only in Bodo (बर’) language. Help the Bodo community with your full 10,000+ features power."
    model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=instruction)

    st.title("बर’ AI Assistant")
    st.write("Gajwnnay! Ma mwnthigwn nwng?")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Hwnnai (Type here)..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("Please enter the correct admin email to use this Bodo AI.")
