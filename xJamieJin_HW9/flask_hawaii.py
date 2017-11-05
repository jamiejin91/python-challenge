import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


app = Flask(__name__)
@app.route("/")
def home():
    return (
        "API for Hawaii Weather from 2010-01-01 to 2017-08-23<br/>"
        "/api/v1.0/precipitation - for precipitation json<br/>"
        "/api/v1.0/stations - for stations json<br/>"
        "/api/v1.0/tobs - for temperature json<br/>"
        "/api/v1.0/date - for date specified json"
    )

@app.route("/api/v1.0/date")
def date():
    return (
        "To get minimum, maximum, and average temperature readings:<br/>"
        "adding yyyy-mm-dd/ will get you the range of the specified date to 2017-08-23<br/>"
        "adding yyyy-mm-dd/yyyy-mm-dd/ will get you the data between the two date range<br/>"
        "dates can only be in between 2010-01-01 to 2017-08-23 inclusive"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    prcp_final = []
    prcp = session.query(Measurement.date, Measurement.prcp).all()
    for i in prcp:
        prcp_final.append({i[0].strftime("%Y-%m-%d"):i[1]})
    return jsonify(prcp_final)

@app.route("/api/v1.0/stations")
def stations():
    stations_final = []
    stations = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).order_by(Station.station).all()
    for i in stations:
        stations_final.append({"station":i[0],"name":i[1],"location":{"latitude":i[2],"longitutde":i[3]},"elevation":i[4]})
    return jsonify(stations_final)

@app.route("/api/v1.0/tobs")
def tobs():
    current = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = current[0].replace(year = (current[0].year - 1))
    year_ago = year_ago.strftime("%Y-%m-%d")
    tobs_final = []
    tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date>=year_ago).order_by(Measurement.date).all()
    for i in tobs:
        tobs_final.append({i[0].strftime("%Y-%m-%d"):i[1]})
    return jsonify(tobs_final)

@app.route("/api/v1.0/<start>")
def onedate(start):
    onedate = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).first()
    onedate_dict = {"min_temp": onedate[0], "max_temp": onedate[1], "avg_temp": onedate[2]}
    return jsonify(onedate_dict)

@app.route("/api/v1.0/<start>/<end>")
def temp_range(start, end):
    twodates = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).first()
    twodates_dict = {"min_temp": twodates[0], "max_temp": twodates[1], "avg_temp": twodates[2]}
    return jsonify(twodates_dict)

if __name__ == "__main__":
    app.run(debug=True)