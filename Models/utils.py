import json
import pickle
import numpy as np
import pandas as pd
import config

class PuneHousePrediction():
    def __init__ (self,area,availability,size,total_sqft,bath,balcony,site_location):
        self.area = area
        self.availability = availability
        self.size = size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.site_location = site_location


    def load_model(self):
        # with open(r"C:\Users\ADMIN\Desktop\Linear Regression Projects\37_Santosh_Mule_Pune_Prediction\Models\project_data_Pune.json",'r') as f:
        #     self.json_dict=json.load(f)

        # with open(r"C:\Users\ADMIN\Desktop\Linear Regression Projects\37_Santosh_Mule_Pune_Prediction\Models\Linear_Model.pkl",'rb') as f:
        #     self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_dict=json.load(f)

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model=pickle.load(f)

    def get_Punehouse_price_prediction(self):
        self.load_model()

        array = np.zeros(len(self.json_dict['columns']))
 
        array[0] = self.json_dict['area'][self.area]
        array[1] = self.json_dict['availability'][self.availability]
        array[2] = self.json_dict['size'][self.size]
        array[3] = self.total_sqft
        array[4] = self.bath
        array[5] = self.balcony
        array[6] = self.json_dict['site_location'][self.site_location]
        

        
        result = self.model.predict([array])[0]
        return round(result,2)

if __name__ == "__main__":
    area_type = 'Carpet  Area'
    availability = 'Ready To Move'
    size = '6 BHK'
    total_sqft = 1500.8
    bath = 3.0
    balcony = 4.0 
    site_location = 'Dapodi'
     




    Obj = PuneHousePrediction(area_type,availability,size,total_sqft,bath,balcony,site_location)
    result = Obj.get_Punehouse_price_prediction()
    print(f"Price Prediction of Pune house is Rs.{result}/- only")