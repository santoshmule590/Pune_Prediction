import re
from Models.utils import PuneHousePrediction
from flask import Flask, jsonify, request, render_template
import config


app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")

@app.route("/Pune_prediction",methods =['POST'])
def get_house_predicted_price():
        
    area_type=request.form.get('area_type')
    availability=request.form.get('availability')    
    size= request.form.get('size')
    total_sqft=float(request.form.get('total_sqft'))
    bath=float(request.form.get('bath'))
    balcony=float(request.form.get('balcony'))
    site_location= request.form.get('site_location')

                    


    Obj = PuneHousePrediction(area_type,availability,size,total_sqft,bath,balcony,site_location)
    result = Obj.get_Punehouse_price_prediction()
        
    return render_template("index.html",prediction=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5002, debug=True)
    