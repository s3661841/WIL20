import pandas as pd

class RainStationDF:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.prepare_data()
        
    def get_data(self):
        return self.data
    
    def load_data(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.prepare_data()

    def prepare_data(self):
        if self.data is not None:
            self.data = self.data[['site_number', 'site_name', 'avg_max_temp', 'avg_min_temp', 
                                 'avg_mean_temp', 'Latitude', 'Longitude', 'Elevation', 
                                 'Koppen_Classification']]
        else:
            raise ValueError("Data not loaded. Please load the data first using load_data method.")
        

class CropConditionDF:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.prepare_data()
        
    def get_data(self):
        return self.data
    
    def load_data(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.prepare_data()
    
    def prepare_data(self):
        if self.data is not None:
            # Select the relevant columns based on the provided CSV structure
            self.crop_condition = self.data[['Crop', 'Lower_PH_range', 'Upper_PH_range', 'Lower_Temp_Range', 
                                             'Upper_Temp_Range', 'Lower_Rainfall_Range', 'Upper_Rainfall_Range',
                                             'Lower_Soil_Temp', 'Upper_Soil_Temp', 'N_Nutrient_Need', 
                                             'K_Nutrient_Need', 'P _Nutrient_Need']]
        else:
            raise ValueError("Data not loaded. Please load the data first using the load_data method.")
