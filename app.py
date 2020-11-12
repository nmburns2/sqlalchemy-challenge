
# Setup and Import Dependencies

import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database into a new model
base = automap_base()

# Reflect the tables
base.prepare(engine, reflect=True)

# Save reference to the table
meas = base.classes.measurement
stat = base.classes.station

# Create session(link) from Python to the DB
sess = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome!<b/><br/>"
        f"<br/>"
        f"Available Routes: <b/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of precipitation data and dates."""

    # Query prcp and date results
    precip = sess.query(meas.prcp, meas.date).all()

    # Convert query results to a dictionary
    precip_dict = []
    for p,d in precip:
        row = {}
        row["Date"] = d
        row["Precipitation"] = p
        precip_dict.append(row)

    # Return JSON representation
    return jsonify(precip_dict)

# Stations Route


if __name__ == "__main__":
    app.run(debug=True)