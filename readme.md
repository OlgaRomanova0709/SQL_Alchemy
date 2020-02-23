# Surfs Up!

![surfs-up.jpeg](Charts/surfs-up.jpeg)

Climate analysis of the area in Honolulu using Pandas, Matplotlib and SQLAlchemy. 

## Step 1 - Climate Analysis and Exploration

I used **Python**(Pandas, and Matplotlib) and **SQLAlchemy**(ORM queries) to do basic climate analysis and data exploration of a climate database. 

* Used SQLAlchemy `create_engine` to connect to the sqlite database.

* Used SQLAlchemy `automap_base()` to reflect tables into classes and saved a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis
 * Ploted the results using the DataFrame `plot` method.
   ![precipitation](Charts/precipitation.png)


### Station Analysis
 * Ploted the results using the DataFrame `plot` method.
  ![frequency](Charts/frequency.png)

- - -

## Step 2 - Climate App

I designed a **Flask API** based on the developed queries.

* Used **FLASK** to create the routes.

### Routes

* `/`

  * Home page.

  * Lists all routes that are available.

* `/api/v1.0/precipitation`

  * Converts the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * queries for the dates and temperature observations from a year from the last data point.
  * Returns a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


* Used Flask **`jsonify`** to convert **API** data into a valid **JSON** response object.


### Temperature Analysis
 * 
   ![temp](Charts/temp.png)

### Daily Rainfall Average.
 * 
  ![normals1](Charts/normals1.png)


