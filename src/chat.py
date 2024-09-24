# chatbot.py
# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

class Chatbot:
    def __init__(self, model_name="llama3"):
        # Define a prompt template for the chatbot
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant. Please respond to the questions"),
                ("user", "Question:{question}")
            ]
        )
        # Initialize the Ollama model
        self.llm = Ollama(model=model_name)
        # Create a chain that combines the prompt and the Ollama model
        self.chain = self.prompt | self.llm

    def ask_question(self, question, dataframes=None):
        # You can process the dataframes here if needed
        if dataframes:
            for df in dataframes:
                st.write(df)  # Display the dataframe in the Streamlit app

        # Invoke the chain with the input text and return the output
        return self.chain.invoke({"question": question})