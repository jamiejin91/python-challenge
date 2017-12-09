from flask import Flask, jsonify, render_template
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, desc

app = Flask(__name__)
engine = create_engine("sqlite:///data/belly_button_biodiversity.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Otu = Base.classes.otu
Samples = Base.classes.samples
Samples_md = Base.classes.samples_metadata
session = Session(engine)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def names():
    sample_names = [name.key for name in Samples.__table__.columns if name.key != "otu_id"]
    return jsonify(sample_names)

@app.route('/otu')
def otu():
    otu_query = session.query(Otu.lowest_taxonomic_unit_found).all()
    return jsonify(otu_query)

@app.route("/metadata/<sample>")
def metadata(sample):
    sample_name = sample[3:]
    md_query = session.query(Samples_md.SAMPLEID,
                              Samples_md.ETHNICITY,
                              Samples_md.GENDER,
                              Samples_md.AGE, 
                              Samples_md.BBTYPE,
                              Samples_md.LOCATION).filter_by(SAMPLEID = sample_name).all()
    result = [{"SAMPLEID":query[0],
              "ETHNICITY":query[1],
              "GENDER":query[2],
              "AGE":query[3],
              "BBTYPE":query[4],
              "LOCATION":query[5]} for query in md_query]
    return jsonify(result)

@app.route('/wfreq/<sample>')
def wfreq(sample):
    sample_name = sample[3:]
    wash_query = session.query(Samples_md.WFREQ).filter_by(SAMPLEID = sample_name).all()
    result = {"WFREQ":wash_query[0][0]}
    return jsonify(result)

@app.route('/samples/<sample>')
def samples(sample):
    samples_query = session.query(Samples.otu_id, "samples.{}".format(sample)).order_by(desc("samples.{}".format(sample))).all()
    result = [{"otu_ids":samples_query[i][0], "sample_values":samples_query[i][1]} for i in range(len(samples_query))]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)