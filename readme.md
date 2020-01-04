# Surfs Up!

![surfs-up.jpeg](Images/surfs-up.jpeg)

You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. 

## Step 1 - Climate Analysis and Exploration

We use **Python**(Pandas, and Matplotlib) and **SQLAlchemy**(ORM queries) to do basic climate analysis and data exploration of our climate database. 

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

  ![precipitation](Charts/precipitation.png)


### Station Analysis

    ![station-histogram](Charts/frequency.png)

- - -

## Step 2 - Climate App

We designed a **Flask API** based on the queries that you have just developed.

* Use **FLASK** to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


* Use Flask **`jsonify`** to convert your **API** data into a valid **JSON** response object.


### Temperature Analysis

    ![temperature](Charts/temp.png)

### Daily Rainfall Average.

  ![daily-normals](Charts/normals1.png)


