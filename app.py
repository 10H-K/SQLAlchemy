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

# Create Session (Link) From Python To The DB
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

    # Create Dictionary From Query Data And Append To List Of past_year_precipitation
    past_year_precipitation = []
    for date, precipitation in query_past_year_precipitation:
        precipitation_dictionary = {}
        precipitation_dictionary[str(date)] = precipitation
        past_year_precipitation.append(precipitation_dictionary)
    return jsonify(past_year_precipitation)


@app.route("/api/v1.0/stations")
def stations():
    query_stations = session.query(Station.station).all()
    stations = list(np.ravel(query_stations))
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def most_active_station_temperatures():
    query_past_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    most_active_station_temperatures = session.query(Measurement.tobs).\
                                        filter(Measurement.station == 'USC00519281').\
                                        filter(Measurement.date >= query_past_year).all()
    temperatures = list(np.ravel(most_active_station_temperatures))
    return jsonify(temperatures)


@app.route("/api/v1.0/<start_date>") #ISO start_date format: (YYYY-MM-DD)
def temperature_statistics_start(start_date):
    # specified_start_date = dt.date.fromisoformat(start_date)
    temperature_statistics = session.query(func.min(Measurement.tobs),
                                           func.max(Measurement.tobs),
                                           func.avg(Measurement.tobs)).\
                                    filter(Measurement.date >= start_date).all()
    statistics = list(np.ravel(temperature_statistics))
    return jsonify(statistics)


@app.route("/api/v1.0/<start_date>/<end_date>")
def temperature_statistics_start_end(start_date, end_date):
    specified_start_date = dt.date.fromisoformat(start_date)
    specified_end_date = dt.date.fromisoformat(end_date)
    temperature_statistics = session.query(func.min(Measurement.tobs),
                                           func.max(Measurement.tobs),
                                           func.avg(Measurement.tobs)).\
                                    filter(Measurement.date >= specified_start_date).\
                                    filter(Measurement.date <= specified_end_date).all()
    statistics = list(np.ravel(temperature_statistics))
    return jsonify(statistics)


if __name__ == '__main__':
    app.run(debug=True)

    