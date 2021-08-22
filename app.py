from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify
from flask import render_template, request

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Lasso
import joblib
import math

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///SQL/CityOfPerth.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
PerthCity = Base.classes.perthcity


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


# for Price Prediction
@app.route("/api/v1.0/predict", methods=['GET','POST'])
def predict():
    data = request.json
    print(data)
    
    suburb = data['Suburb']
    
    house = pd.read_csv("static/data/house.csv")

    # Assign the data to X and y
    X = house[["bedrooms", "bathrooms", "car_space", "land_size", "building_size", "built_date", "perth", "west_perth", "east_perth", "northbridge", "crawley", "nedlands"]]
    y = house["price"].values.reshape(-1, 1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # Create a StandardScater model and fit it to the training data
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)

    # Load the best Model
    # my_model = joblib.load("best_model.pkl")
    my_model = joblib.load("ML_Model/best_model.pkl")
    # my_model = load_model("keras_model_trained.h5")

    # X_test = X_scaler.transform([[data['Bedroom'],data['Bathroom'],data['Car_Spaces'],data['Land_Size'],data['Built_Size'],data['Built_Year'],1,0,0,0,0,0]])

    if suburb == "perth":
        X_test = X_scaler.transform([[data['Bedroom'],data['Bathroom'],data['Car_Spaces'],data['Land_Size'],data['Built_Size'],data['Built_Year'],1,0,0,0,0,0]])
    elif suburb == "westp":
        X_test = X_scaler.transform([[data['Bedroom'],data['Bathroom'],data['Car_Spaces'],data['Land_Size'],data['Built_Size'],data['Built_Year'],0,1,0,0,0,0]])
    elif suburb == "eastp":
        X_test = X_scaler.transform([[data['Bedroom'],data['Bathroom'],data['Car_Spaces'],data['Land_Size'],data['Built_Size'],data['Built_Year'],0,0,1,0,0,0]]) 
    elif suburb == "northbridge":
        X_test = X_scaler.transform([[data['Bedroom'],data['Bathroom'],data['Car_Spaces'],data['Land_Size'],data['Built_Size'],data['Built_Year'],0,0,0,1,0,0]]) 
    elif suburb == "crawley":
        X_test = X_scaler.transform([[data['Bedroom'],data['Bathroom'],data['Car_Spaces'],data['Land_Size'],data['Built_Size'],data['Built_Year'],0,0,0,0,1,0]]) 
    elif suburb == "nedlands":
        X_test = X_scaler.transform([[data['Bedroom'],data['Bathroom'],data['Car_Spaces'],data['Land_Size'],data['Built_Size'],data['Built_Year'],0,0,0,0,0,1]]) 

    print(X_test)

    predictions = my_model.predict(X_test)
    exact_value = y_scaler.inverse_transform(predictions)[0].round(decimals=0)
    mse = 0.1300
    min_value = math.trunc(exact_value * (1-mse))
    max_value = math.trunc(exact_value * (1+mse))
    result = f"${min_value} - ${max_value}"
    print(result)

    return {"result": result } #all data function should be here


# Perth City API
@app.route("/api/v1.0/perthcity")
def perthcity():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of install data"""
    # Query all outputs
    results = session.query(PerthCity.sale_id, PerthCity.full_address, PerthCity.price, PerthCity.sold_date, PerthCity.property_type, PerthCity.bedrooms,
       PerthCity.bathrooms, PerthCity.car_space, PerthCity.land_size, PerthCity.building_size, PerthCity.built_date, PerthCity.rent, PerthCity.rent_date, 
       PerthCity.agent, PerthCity.lat, PerthCity.lng, PerthCity.address, PerthCity.suburb, PerthCity.state, PerthCity.postcode).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_properties = []
    for sale_id, full_address, price, sold_date, property_type, bedrooms, bathrooms, car_space, land_size, building_size, built_date, rent, rent_date, agent, \
        lat, lng, address, suburb, state, postcode in results:
        
        property_dict = {}

        property_dict["sale_id"] = sale_id
        property_dict["full_address"] = full_address
        property_dict["price"] = price
        property_dict["sold_date"] = sold_date
        property_dict["property_type"] = property_type
        property_dict["bedrooms"] = bedrooms
        property_dict["bathrooms"] = bathrooms
        property_dict["car_space"] = car_space
        property_dict["land_size"] = land_size
        property_dict["building_size"] = building_size
        property_dict["built_date"] = built_date
        property_dict["rent"] = rent
        property_dict["rent_date"] = rent_date
        property_dict["agent"] = agent
        property_dict["lat"] = lat
        property_dict["lng"] = lng
        property_dict["address"] = address
        property_dict["suburb"] = suburb
        property_dict["state"] = state
        property_dict["postcode"] = postcode

        all_properties.append(property_dict)

    return jsonify(all_properties)



if __name__ == '__main__':
    app.run(port=5500, debug=True)