import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from src.chat import Chatbot
from src.dataframes import RainStationDF
from src.Visualisations import ScatterplotVisualizer

# Title
st.title('Prototype')

#Load the data
rain_stations_df = './Data/rain_stations_df.csv'
rain_scatter = RainStationDF(rain_stations_df)

# Handle other selections
selected = st.selectbox("Select Data", ["Rain Stations Data", "Table 2 Data", "Table 3 Data", "Chatbot"])

# Sidebar with tabs
with st.sidebar:
    selected = option_menu(
        menu_title="Select Data",
        options=["Rain Stations Data", "Table 2 Data", "Table 3 Data", "Chatbot"],
        icons=["cloud-rain", "table", "table"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Rain Stations Data":
    #Define the scatterplot layer
    visualizer = ScatterplotVisualizer(rain_scatter)
    visualizer.render()

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

# Chatbot feature
st.subheader('Chat with the Bot')
chatbot = Chatbot()

if __name__ == '__main__':
    question = st.text_input('Enter your question here:')
    if st.button('Ask'):
        response = chatbot.ask_question(question)
        st.write(response)