import numpy as np
import datetime as dt
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
Base = automap_base()
from sqlalchemy import create_engine, func
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base.prepare(engine, reflect=True)
from flask import Flask, jsonify

Measurement = Base.classes.measurement
Station = Base.classes.station

from sqlalchemy.orm import Session
session = Session(engine)
app=Flask(__name__)


@app.route('/')
def welcome():
    return(f"Welcome to homePage<br/>"
           f"Available pages:1. /api/v1.0/precipitation<br/>"
           f"________________2./api/v1.0/stations<br/>"
           f"________________3./api/v1.0/tobs<br/>"
           f"________________4./api/v1.0/start<br/>"
           f"________________5./api/v1.0/start/end<br/>"
          )
@app.route('/api/v1.0/precipitation')
def precipitation():
    result=session.query(Measurement.date,Measurement.prcp).all()
    all_result = []
    for date, prcp in result:
        result_dict = {}
        result_dict["date"] = date
        result_dict["precipitation"] = prcp
        all_result.append(result_dict)
    return jsonify(all_result)

@app.route('/api/v1.0/stations')
def stations():
    stations=session.query(Measurement.station).all()
    
    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def tobs():
    last_year=dt.date(2017, 8, 23)-dt.timedelta(days=365)
    Measurement_last_year=session.query(Measurement.prcp,Measurement.date).filter(Measurement.date>=last_year).\
                                                           order_by(Measurement.date).all()

    return jsonify(Measurement_last_year)

@app.route('/api/v1.0/<start>')
def daily_normals(start):
    format_date=datetime.strptime(start,"%Y%m%d")
    start_date=format_date.strftime('%y-%m-%d')
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    temperature=session.query(*sel).filter(Measurement.date >= start_date).all()
    return jsonify(temperature)

@app.route('/api/v1.0/<start>/<end>')
def daily_normals_btw(start,end):
    format_start=datetime.strptime(start,"%Y%m%d")
    start_date=format_start.strftime('%y-%m-%d')
    format_end=datetime.strptime(end,"%Y%m%d")
    end_date=format_end.strftime('%y-%m-%d')
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    temperature_btw=session.query(*sel).filter(Measurement.date >= start_date).filter(Measurement.date >= end_date).all()
    return jsonify(temperature_btw)


if __name__ == '__main__':
    app.run(debug=True)
