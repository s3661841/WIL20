import streamlit as st
import pandas as pd
import numpy as np

class CropRecommendation:
    def __init__(self, crop_data_path, station_data_path):
        # Load crop and station data
        self.crop_data = pd.read_csv(crop_data_path)
        self.station_data = pd.read_csv(station_data_path)

    def get_station_data(self, station_name):
        # Check if 'Station_Name' column exists
        self.station_data = self.station_data[['Longitude', 'Latitude', 'Elevation', 'Station Name']]
        self.station_data.rename(columns={'Station_Name': 'Station Name'}, inplace=True)
        self.station_data.columns = ['Longitude', 'Latitude', 'Elevation', 'Station_Name']
        self.station_data['Elevation'] = self.station_data['Elevation'].astype(int)
        
        if 'Station_Name' not in self.station_data.columns:
            raise KeyError("The column 'Station_Name' does not exist in the station data.")
        
        # Filter the DataFrame for the given station name
        self.station = self.station_data[self.station_data['Station_Name'] == station_name]
        return self.station
    
    def get_station_elevation(self, station_name):
        # Get the station data for the given station name
        self.station = self.get_station_data(station_name)
        
        # Extract the elevation from the station data
        self.elevation = self.station['Elevation'].values[0]
        
        # Get the recommended crops based on the elevation
        self.recommended_crops = self.recommend_crop(self.elevation)
        
        return self.recommended_crops
    
    def reconmend_crop(self, elevation):
        # Define the crop recommendation logic based on elevation
        
        self.suggested_crops = []
        
        
        for crops in self.crop_data.itertuples():
            if elevation >= crops[''] and elevation <= crops.Upper_Elevation:
                self.min_values[crops.Crop] = crops.Min_Temperature
                self.max_values[crops.Crop] = crops.Max_Temperature
        
