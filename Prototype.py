import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Title
st.title('Prototype')

# Header
st.header('Data Tables')

# Subheader
st.subheader('Rain Stations Data')

# Load rain_stations_df
rain_stations_df = './Data/rain_stations_df.csv'

rain_stations_data = pd.read_csv(rain_stations_df)


# Display data
'''
st.table(rain_stations_data)

'''

# Scatter plot
# Prepare data for scatter chart
# This code snippet is preparing data for a scatter chart visualization using Streamlit in Python.
# Here's a breakdown of what each part of the code is doing:
scatter_data = rain_stations_data[['Longitude', 'Latitude', 'Elevation', 'Station Name']]
scatter_data.columns = ['Longitude', 'Latitude', 'Elevation', 'Station_Name']

# Create scatter chart
scatter_data = scatter_data[scatter_data['Longitude'] >= 110]
st.scatter_chart(scatter_data, x='Longitude', y='Latitude', size='Elevation', color='Station_Name')

'''
    
# Subheader
st.subheader('Table 2 Data')

'''

# Load Table 2_table
'''
Table_2_table_df = './Data/Table 2_table.csv'
Table_2_table_data = pd.read_csv(Table_2_table_df)

'''

# Display data


'''
st.table(Table_2_table_data)

'''

# Subheader
'''

st.subheader('Table 3 Data')

'''

# Load Table 3_table

'''

Table_3_table_df = './Data/Table 3_table.csv'
Table_3_table_data = pd.read_csv(Table_3_table_df)

'''

# Display data

'''
st.table(Table_3_table_data)

'''