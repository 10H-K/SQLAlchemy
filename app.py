# Import Dependencies
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# Create Engine To hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect An Existing Database Into A New Model
Base = automap_base()

# Use Base Class To Reflect Database Tables
Base.prepare(autoload_with=engine)

# Save References To Each Table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create Session (Link) From Python To The Database
session = Session(engine)


#################################################
# Flask Setup
#################################################


app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start_date&gt;<br/>"
        f"/api/v1.0/&lt;start_date&gt;/&lt;end_date&gt;<br/>"
        f"<br/>To search by date type, please replace &lt;date_type&gt; with International Organization for Standardization (ISO) date format (YYYY-MM-DD)."
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculation For Date One Year From Last Date In Dataset
    query_past_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query To Retrieve Date And Precipitation Scores
    query_past_year_precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= query_past_year).all()

    # Create Dictionary From Query And Append To List past_year_precipitation
    past_year_precipitation = []
    for date, precipitation in query_past_year_precipitation:
        precipitation_dictionary = {}
        precipitation_dictionary[str(date)] = precipitation
        past_year_precipitation.append(precipitation_dictionary)
    
    # Return Past Year Precipitation Data As JSON
    return jsonify(past_year_precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # Query To Find All Stations In Dataset
    query_stations = session.query(Station.station).all()

    # Convert Query To Flattened List
    stations = list(np.ravel(query_stations))

    # Return All Stations As JSON
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def most_active_station_temperatures():
    # Calculation For Date One Year From Last Date In Dataset
    query_past_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query Last 12 Months Of Temperature Observation Data For Most Active Station
    most_active_station_temperatures = session.query(Measurement.tobs).\
                                        filter(Measurement.station == 'USC00519281').\
                                        filter(Measurement.date >= query_past_year).all()
    
    # Convert Query To Flattened List
    temperatures = list(np.ravel(most_active_station_temperatures))

    # Return Most Active Station Temperatures As JSON
    return jsonify(temperatures)


@app.route("/api/v1.0/<start_date>") #ISO start_date Format: (YYYY-MM-DD)
def temperature_statistics_start(start_date):
    # Query The Database For Temperature Statistics (Minimum, Maximum, Average)
    temperature_statistics = session.query(func.min(Measurement.tobs),
                                           func.max(Measurement.tobs),
                                           func.avg(Measurement.tobs)).\
                                    filter(Measurement.date >= start_date).all()
    
    # Convert Query To Flattened List
    statistics = list(np.ravel(temperature_statistics))

    # Return Temperature Statistics As JSON
    return jsonify(statistics)


@app.route("/api/v1.0/<start_date>/<end_date>") #ISO start_date And end_date Format: (YYYY-MM-DD)
def temperature_statistics_start_end(start_date, end_date):
    # Query The Database For Temperature Statistics (Minimum, Maximum, Average)
    temperature_statistics = session.query(func.min(Measurement.tobs),
                                           func.max(Measurement.tobs),
                                           func.avg(Measurement.tobs)).\
                                    filter(Measurement.date >= start_date).\
                                    filter(Measurement.date <= end_date).all()
    
    # Convert Query To Flattened List
    statistics = list(np.ravel(temperature_statistics))

    # Return Temperature Statistics As JSON
    return jsonify(statistics)


if __name__ == '__main__':
    app.run(debug=True)

    