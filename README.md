# WeatherPy

## Overview ##

The goal of this portion of the project is to develop a Python script for visualizing weather data from more than 500 cities located at varying distances from the equator. This will be accomplished through the use of the CitiPy Python library and the OpenWeatherMap API, which will enable the creation of a representative model showcasing weather patterns across these cities.

## Process ##

A) Geographic Coordinate & City List Generation:
  1. Importation of dependencies (Matplotlib, Pandas, NumPy, Requests, Time, PPrint, SciPy, OpenWeatherMap API Key, and CitiPy)
  2. Creation of empty lists to store Latitude and Longitude combinations, along with city names
  3. Specification of range of Latitudes and Longitudes
  4. Creation of set of random Latitude and Longitude combinations
  5. Identification of nearest city for each Latitude and Longitude combination
     - If the identified city is unique, it is added to the cities list
  6. Print statements to confirm sufficient count of cities and proper execution of code

B) Usage of OpenWeatherMap API to Retrieve Weather Data for Generated Cities:
  1. Setting OpenWeatherMap current weather data API base url
  2. Defining empty list to contain the fetched weather data for each city
  3. Print message indicating start of weather data retrieval
  4. Creation of counters used for dividing cities list into sets of 50 cities
  5. For loop through cities list to fetch weather data for each city
     1. Grouping cities into sets of 50 for logging purposes
     2. Creation of endpoint url with each city included
     3. Print statement logging url, record, and set numbers
     4. Adding 1 to record count, for next city weather data retrieval
     5. Running API request for each city
        - Parsing JSON for Latitude, Longitude, Max Temp, Humidity, Cloudiness, Wind Speed, Country, Date
        - Appending city information to city_data list
        - In case error is experienced, skipping city causing error
  6. Print statements indicating data loading is complete
  7. Converting city weather data into Pandas DataFrame
  8. Showing record count for DataFrame
  9. Displaying DataFrame sample data
  10. Exporting city data DataFrame into csv
  11. Reading and displaying saved data

C) Creation of Scatter Plots to Showcase the Relationship Between Weather Variables and Latitude:

![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/816e2fa6-fd62-4237-8e7d-f4e2d6ae196b) 
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/b9751b35-8d6e-4c31-adcb-ed358dc2321b)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/2af914f6-913a-47bb-8bf3-5328da38709f)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/8a21b723-76f1-49b6-b762-9dc8a22774eb)

D) Computation of Linear Regression for Each Relationship Between Weather Variables and Latitude:
  1. Creation of function used to create linear regression plots
  2. Creation of DataFrame with Northern Hemisphere data (Latitude >= 0)
  3. Displaying Northern Hemisphere DataFrame
  4. Creation Of DataFrame with Southern Hemisphere data (Latitude < 0)
  5. Displaying Southern Hemisphere DataFrame
  6. Creation of Linear Regression Plots with subsequent analysis

![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/8082e89c-7575-4388-bfe4-8c10679b6a15)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/a9f3ee60-c75d-4206-912f-b8bf46267511)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/b14ab3ca-980b-4248-b29d-fd25040ecb27)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/179e508a-9803-44da-83d3-edcdbc93aac4)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/60978ebc-5532-4ce7-9cc0-ab2053f25420)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/0e96d90a-288a-4216-ab5a-a38aea72ab14)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/72071b48-27bc-4ea2-9569-29a7b9eaf82c)
![output](https://github.com/10H-K/Python_API_Weather/assets/152930492/9e80e745-4504-41a3-a21c-8bbc3f286c8b)

---

# VacationPy

## Overview ##

The goal of this portion of the project is to develop a Python script for creating map visualizations of the cities discovered in the first portion of the project. This will be accomplished through the use of the geoViews Python library and the Geoapify API.

## Process ##

A) Loading Previously Generated Weather and Coordinate Data:
  1. Importation of dependencies (hvPlot, Pandas, Requests, PPrint, and Geoapify API Key)
  2. Loading CSV file containing city weather data from WeatherPy into Pandas DataFrame
  3. Displaying 'city_data_df' DataFrame

B) Creation of Geographical Map for every City in 'city_data_df' DataFrame:
  1. Configuration of the map plot
  2. Displaying map plot

<img width="844" alt="Screenshot 2024-03-13 at 12 20 58 PM" src="https://github.com/10H-K/Python_API_Weather/assets/152930492/2f1a8404-586e-4cfb-96a9-49da327bc72a">


C) Truncatation of 'city_data_df' DataFrame based on Ideal Weather Conditions:
  1. Narrowing down 'city_data_df' to cities that fit ideal weather criteria
  2. Dropping any rows with null values
  3. Display truncated ideal weather city DataFrame

D) Creation of new DataFrame called 'hotel_df':
  1. Creation of DataFrame called hotel_df to store City, Country, Coordinates, and Humidity
  2. Adding empty column, "Hotel Name", to DataFrame to store hotel found using Geoapify API
  3. Displaying hotel_df DataFrame

E) Utilizing Geoapify API to find First Hotel Located Within 10,000 Metres of City Coordinates:
  1. Setting filter and API parameters to search for hotel
  2. Print message for initialization of hotel search
  3. Iteration through hotel_df DataFrame via For Loop
     1. Retrieving Latitude and Longitude from hotel_df DataFrame
     2. Adding filter and bias parameters with current city Latitude and Longitude to params dictionary
     3. Setting places Geoapify API base url
     4. Making API request using params dictionaty, converting API response to JSON format
     5. Grabbing first hotel from results and storing name in hotel_df DataFrame
        - If no hotel found, setting hotel name as "No hotel found" 
     6. Logging search results
  4. Displaying found hotel data

F) Addition of Hotel Name and Country as Additional Information in Hover for Truncated Cities in Geographical Map:
  1. Configuration of the map plot
  2. Displaying map plot

<img width="819" alt="Screenshot 2024-03-13 at 12 21 09 PM" src="https://github.com/10H-K/Python_API_Weather/assets/152930492/63e7eef5-93c9-4b3b-9ede-e5314fd1967c">
