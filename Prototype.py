import streamlit as st
from src.chat import Chatbot
from src.dataframes import RainStationDF, CropConditionDF
from src.Visualisations import ScatterplotVisualizer
from src.search_crop import CropRecommendation

#layout setting
st.set_page_config(layout="wide")

# Title
st.title('Crop Recommendation System')
if st.button('Home'):
    st.rerun()

# Load the data
rain_stations_df = './src/data/averages_by_station.csv'
rain_scatter = RainStationDF(rain_stations_df)

CropCondition_df = './src/data/CropConditionData.csv'
CropCondition_data = CropConditionDF(CropCondition_df)

# Initialize the functions
visualizer = ScatterplotVisualizer(rain_scatter)
Recommendation = CropRecommendation(CropCondition_df, rain_stations_df)

# Full width for each section
st.subheader('Chatbot')
with st.container():
    chatbot = Chatbot()
    question = st.text_input('Enter your question:', key='chat')
    if st.button('Ask Question', key='ask'):
        response = chatbot.ask_question(question)
        st.write(response)

st.markdown("---")  # Line divider between sections

# Bottom section: Map and Recommend using full width
map_recommend_cols = st.columns([1, 1])  # Use equal width for both columns

with map_recommend_cols[0]:
    st.subheader('Map')
    st.write('Weather Map')
    visualizer.render()  # Render the map visualizer

with map_recommend_cols[1]:
    st.subheader('Recommend')
    st.write('Enter the station name to get crop recommendations:')
    station_name = st.text_input('Station Name:', key='station')
    if st.button('Get Recommendations', key='recommend'):
        station = Recommendation.get_station_data(station_name)
        st.write(station)
        if station is not None:
            suitable_crops = Recommendation.reconmend_crop(station['Elevation'])
            st.table(suitable_crops)
