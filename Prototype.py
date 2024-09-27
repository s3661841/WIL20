import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from src.chat import Chatbot
from src.dataframes import RainStationDF, CropConditionDF
from src.Visualisations import ScatterplotVisualizer
from src.search_crop import CropRecommendation

# Title
st.title('Prototype')

#Load the data
rain_stations_df = './src/data/rain_stations_df.csv'
rain_scatter = RainStationDF(rain_stations_df)


CropCondition_df = './src/data/CropConditionData.csv'
CropCondition_data = CropConditionDF(CropCondition_df)

#intitalise the functions
visualizer = ScatterplotVisualizer(rain_scatter)
Reconmendation = CropRecommendation(CropCondition_df, rain_stations_df)


#set the layout

#Set the columns
rain_col, crops_col, chat_col = st.columns(3)

#set the rain tabs
rain_visuals_tab, rain_data_tab   = st.tabs(['Rain Visuals', 'Rain Data'])

#set the crops tabs
crops_visuals_tab, crops_data_tab  = st.tabs(['Crops Visuals', 'Crops Data'])

# Sidebar with tabs
with st.sidebar:
    selected = option_menu(
        menu_title="Select Data",
        options=["Rain Stations Data", "Crop Conditions", "Table 3 Data", "Chatbot"],
        icons=["cloud-rain", "table", "table"],
        menu_icon="cast",
        default_index=0,
    )

with st.container():
    if selected == "Rain Stations Data":
        #Define the scatterplot layer
        with rain_col:
            with rain_visuals_tab:
                st.subheader('Rain Map')
                visualizer.render()
            with rain_data_tab:
                st.subheader('Rain Data')
                st.write(rain_scatter.get_data())
        with crops_col:
            with crops_visuals_tab:
                st.subheader('Crop Reconmendations')
                st.write('Enter the station name to get crop recommendations')
                station_name = st.text_input('Enter the station name:')
                if st.button('Get Recommendations'):
                    station = Reconmendation.get_station_data(station_name)
                    st.write(station)
                    if station is not None:
                        suitable_crops = Reconmendation.recommend_crop(station['Elevation'])
                        st.table(suitable_crops)
            with crops_data_tab:
                st.subheader('Crops Data')
                st.write(CropCondition_data.get_data())

    elif selected == "Crop Conditions":
        st.subheader('Crop Conditions')
        st.table(CropCondition_data)
    
    elif selected == "Table 3 Data":
        st.subheader('Table 3 Data')
        Table_3_table_df = './Data/Table 3_table.csv'
        Table_3_table_data = pd.read_csv(Table_3_table_df)
        st.table(Table_3_table_data)
    
    elif selected == "Chatbot":
        st.subheader('Chatbot')


with st.container():
    # Chatbot feature
    st.subheader('Chat with the Bot')
    chatbot = Chatbot()

if __name__ == '__main__':
    question = st.text_input('Enter your question here:')
    if st.button('Ask'):
        response = chatbot.ask_question(question)
        st.write(response)