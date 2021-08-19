import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import render_template, redirect , request
import logging

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
@app.route("/home/", methods=['GET','POST'] )
def home():

    if request.method == "POST":
        
        #get form data
        bedroom = request.form.get('bedroom_range')
        bathroom = request.form.get('bathroom_range')
        carspace = request.form.get('carspaces_range')
        landsize = request.form.get('land')
        builtsize = request.form.get('built')
        builtyear = request.form.get('builtdate')
        suburb = request.form.get('suburbs')
        test_data = [bedroom,bathroom,carspace,landsize,builtsize,builtyear,suburb]
        app.logger.info(test_data)
         #call preprocessDataAndPredict and pass inputs
        # try:
            # test_data = [bedroom,bathroom,carspace,landsize,builtsize,builtyear,suburb]
            # print(test_data)
        #     # prediction = preprocessDataAndPredict(
        #     #     bedroom,bathroom,carspace,landsize,builtsize,builtyear,suburb)
        #     # #pass prediction to template
    return render_template('index.html')
   
        # except ValueError:
        #     return "Please Enter valid values"
  
        # pass
        # pass
# def preprocessDataAndPredict(
#     bedroom,bathroom,carspace,landsize,builtsize,builtyear,suburb):
    
#     #keep all inputs in array
#     test_data = [bedroom,bathroom,carspace,landsize,builtsize,builtyear,suburb]
#     print(test_data)
    
    # #convert value data into numpy array
    # test_data = np.array(test_data)
    
    # #reshape array
    # test_data = test_data.reshape(1,-1)
    # print(test_data)
    
    # #open file
    # file = open("randomforest_model.pkl","rb")
    
    # #load trained model
    # trained_model = joblib.load(file)
    
    # #predict
    # prediction = trained_model.predict(test_data)
    
    # return prediction
    
    # pass

    # pass

@app.route("/api/v1.0/predict", methods=['GET','POST'])
def predict():
    data = request.json
    print(data)
    return {"result": "Hi!"} #all data function should be here



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