from flask import Flask, jsonify
from flask import render_template, redirect

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import render_template, redirect , request

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

    # Return template and data
    return render_template("index.html")




@app.route("/about")
def about():

    # Return template and data
    return render_template("about.html")




@app.route("/estimation" )
def estimation():

    # Return template and data
    return render_template("estimation.html")



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