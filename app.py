import streamlit as st
import google.generativeai as genai

# Configure Gemini using Streamlit Secrets (prevents GitHub block)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize Gemini 3.6 Flash
model = genai.GenerativeModel("gemini-3.6-flash")

st.set_page_config(page_title="AI Personal Assistant", page_icon="🤖")

st.title("🤖 AI Personal Assistant")
st.write("Ask me anything! Powered by Google Gemini.")

question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if question:
        with st.spinner("Generating answer..."):
            response = model.generate_content(question)
            st.success(response.text)
    else:
        st.warning("Please enter a question first.")
