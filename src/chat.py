# chatbot.py
# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.document_loaders import CSVLoader
import streamlit as st
import pandas as pd


class Chatbot:
    def __init__(self, model_name="llama3"):
        
        # Load the data
        self.weather_file_path = "./src/data/averages_by_station.csv"
        self.weather_data = pd.read_csv(self.weather_file_path)
        
        self.crop_path = "./src/data/CropConditionData.csv"
        self.crop_data = pd.read_csv(self.crop_path)
        
        # Convert the DataFrame to a string representation to include in the prompt
        self.weather_data_str = self.weather_data.to_csv(index=False)
        self.crop_data_str = self.crop_data.to_csv(index=False)
        
        # prompt also includes csv file
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", f"You are a crop scientist and you are getting asked where in Australia would be best to grow crops per user's question. \
                 Please refer to the attached files for related data.\n\n{self.weather_data_str} \n\n{self.crop_data_str}"), 
                ("user", "Question:{question}")
            ]
        )
        
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