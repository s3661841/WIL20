import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from src.chat import Chatbot

# Title
st.title('Prototype')

# Load rain_stations_df
rain_stations_df = './Data/rain_stations_df.csv'
rain_stations_data = pd.read_csv(rain_stations_df)

# Prepare data for map visualization
rain_scatter = rain_stations_data[['Longitude', 'Latitude', 'Elevation', 'Station Name']]
rain_scatter.columns = ['Longitude', 'Latitude', 'Elevation', 'Station_Name']

# Sidebar with tabs
with st.sidebar:
    selected = option_menu(
        menu_title="Select Data",
        options=["Rain Stations Data", "Table 2 Data", "Table 3 Data", "Chatbot"],
        icons=["cloud-rain", "table", "table"],
        menu_icon="cast",
        default_index=0,
    )

# Display selected data
if selected == "Rain Stations Data":
    st.subheader('Rain Stations Data')
    st.scatter_chart(rain_scatter, x='Longitude', y='Latitude', size='Elevation', color='Station_Name')
elif selected == "Table 2 Data":
    st.subheader('Table 2 Data')
    Table_2_table_df = './Data/Table 2_table.csv'
    Table_2_table_data = pd.read_csv(Table_2_table_df)
    st.table(Table_2_table_data)
elif selected == "Table 3 Data":
    st.subheader('Table 3 Data')
    Table_3_table_df = './Data/Table 3_table.csv'
    Table_3_table_data = pd.read_csv(Table_3_table_df)
    st.table(Table_3_table_data)
elif selected == "Chatbot":
    st.subheader('Chatbot')
    st.chatbot
    
    
# Chatbot feature
st.subheader('Chat with the Bot')
chatbot = Chatbot()

if __name__ == "__main__":
    chatbot
