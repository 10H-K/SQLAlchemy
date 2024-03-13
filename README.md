# Analysis and Exploration of Climate Data

## Overview ##

The goal of this portion of the project is to conduct a basic climate analysis and data exploration of the climate database using Python and SQLAlchemy. This will involve utilizing SQLAlchemy ORM queries, along with Pandas and Matplotlib for data manipulation and visualization, respectively.

## Process ##

A) Reflection of Tables into SQLAlchemy ORM:
  1. Importation of dependencies (Matplotlib, NumPy, Pandas, DateTime, and SQLAlchemy)
  2. Using SQLAlchemy create_engine() function to connect to the SQLite database
  3. Using the SQLAlchemy automap_base() function to reflect the tables into classes, and then saving references to the classes named station and measurement
  4. Linking Python to the database by creating a SQLAlchemy session

B) Exploratory Precipitation Analysis:
  1. Finding the most recent date in the dataset
  2. Using the most recent date to get the previous 12 months of precipitation data by querying the previous 12 months of data
  3. Selecting only the "date" and "prcp" values
  4. Loading the query results into a Pandas DataFrame, explicitly setting the column names
  5. Sorting the DataFrame values by "date"
  6. Plotting the results by using the DataFrame plot method
  7. Using Pandas to print the summary statistics for the precipitation data

![output](https://github.com/10H-K/SQLAlchemy_Hawaii/assets/152930492/8c1be324-21ee-45b5-9e4b-aa67bf0b5422)

C) Exploratory Station Analysis:
  1. Designing a query to calculate the total number of stations in the dataset
  2. Designing a query to find the most-active stations (that is, the stations that have the most rows) by completing the following steps:
     - Listing the stations and observation counts in descending order
     - Answering the following question: which station id has the greatest number of observations?
  3. Designing a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query
  4. Designing a query to get the previous 12 months of temperature observation (TOBS) data by completing the following steps:
     - Filtering by the station that has the greatest number of observations
     - Querying the previous 12 months of TOBS data for that station
     - Plotting the results as a histogram with bins=12
  5. Closing the session

![output](https://github.com/10H-K/SQLAlchemy_Hawaii/assets/152930492/8e1db508-f427-49db-8480-b2343d02c142)

---

# Design of Climate App

## Overview ##

The goal of this portion of the project is to leverage the initial data analysis and design a Flask API based on the previously developed queries.

## Process ##

A)  Use Flask To Create Routes:
  1. /
     - Start at the homepage
     - List all the available routes
  2. /api/v1.0/precipitation
     - Convert query results from the precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value
     - Return the JSON representation of the dictionary
  3. /api/v1.0/stations
     - Return a JSON list of stations from the dataset 
  4. /api/v1.0/tobs
     - Query the dates and temperature observations of the most-active station for the previous year of data
     - Return a JSON list of temperature observations for the previous year
  5. /api/v1.0/&lt;start&gt; and /api/v1.0/&lt;start&gt;/&lt;end&gt;
     - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range
     - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date
     - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive

    
