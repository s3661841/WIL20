import pandas as pd

class RainStationDF:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        
    def get_data(self):
        return self.data
    
    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        self.prepare_data()

    def prepare_data(self):
        if self.data is not None:
            self.rain_scatter = self.data[['Longitude', 'Latitude', 'Elevation', 'Station Name']]
            self.rain_scatter.rename(columns={'Station Name': 'Station_Name'}, inplace=True)
            self.rain_scatter.columns = ['Longitude', 'Latitude', 'Elevation', 'Station_Name']
        else:
            raise ValueError("Data not loaded. Please load the data first using load_data method.")