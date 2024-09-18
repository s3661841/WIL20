import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

class Chatbot:
    def __init__(self):
        self.openai_api_key = None
        self.setup_ui()

    def setup_ui(self):
        st.title("Soil Chatbot")
        self.openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
        self.create_form()

    def create_form(self):
        with st.form("my_form"):
            text = st.text_area(
                "Enter text:",
                "What is the best soil for growing tomatoes?",
            )
            submitted = st.form_submit_button("Submit")
            if not self.openai_api_key.startswith("sk-"):
                st.warning("Please enter your OpenAI API key!", icon="⚠")
            if submitted and self.openai_api_key.startswith("sk-"):
                self.generate_response(text)

    def generate_response(self, input_text):
        model = ChatOpenAI(temperature=0.7, api_key=self.openai_api_key)
        st.info(model.invoke(input_text))



