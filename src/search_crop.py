import streamlit as st
import pandas as pd
import numpy as np

class CropRecommendation:
    def __init__(self, crop_data_path, station_data_path):
        # Load crop and station data
        self.crop_data = pd.read_csv(crop_data_path)
        self.station_data = pd.read_csv(station_data_path)
        
    def get_station_data(self, station_name):
        # Ensure station_name is a scalar value and not a Series
        if isinstance(station_name, pd.Series):
            station_name = station_name.iloc[0]
            st.write(station_name)
        
        self.station = self.station_data[self.station_data['site_name'] == station_name]
        return self.station

    def get_station_avg_temps(self, station_name):
        self.station = self.get_station_data(station_name)
        
        # Check if station data is found
        st.write(self.station)
        st.write(self.station.empty)
        st.write(station_name)
        if self.station.empty:
            st.error(f"No data found for station: {station_name}")
            return None, None, None  # Return None or some default value
        
        # If station exists, extract the temperatures
        self.avg_min_temp = self.station['avg_min_temp'].values[0]
        self.avg_max_temp = self.station['avg_max_temp'].values[0]
        self.avg_mean_temp = self.station['avg_mean_temp'].values[0]
        
        return self.avg_min_temp, self.avg_max_temp, self.avg_mean_temp


    def reconmend_crop(self, station_name):
        self.suggested_crops = []
        
        # Get the average mean temperature for the station
        avg_mean_temp = self.get_station_avg_temps(station_name)[1]
        
        # Check if avg_mean_temp is valid
        if avg_mean_temp is None:
            return []  # Return an empty list if the station data is not found
        
        # Iterate through the crop data to find crops that fit the mean temperature range
        for crop in self.crop_data.itertuples():
            if crop.avg_min_temp <= avg_mean_temp <= crop.avg_max_temp:
                self.suggested_crops.append(crop.Crop)
                
        return self.suggested_crops
