from flask import Flask, jsonify
from flask import render_template, redirect


#################################################
# Database Setup
#################################################


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




@app.route("/estimation")
def estimation():

    # Return template and data
    return render_template("estimation.html")





if __name__ == '__main__':
    app.run(port=5500, debug=True)