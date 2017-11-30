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

otu = Base.classes.otu
samples = Base.classes.samples
samples_md = Base.classes.samples_metadata
session = Session(engine)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def names():
    sample_names = [name.key for name in samples.__table__.columns if name.key != "otu_id"]
    return jsonify(sample_names)

@app.route('/otu')
def otu():
    otu_query = session.query(otu.otu_id,otu.lowest_taxonomic_unit_found).all()
    result = {"otu_id":otu_query[0],
             "lowest_taxonomic_unit_found":otu_query[1]}
    return jsonify(result)

@app.route("/metadata/<sample>")
def metadata(sample):
    md_query = session.query(samples_md.SAMPLEID,
                              samples_md.ETHNICITY,
                              samples_md.GENDER,
                              samples_md.AGE, 
                              samples_md.BBTYPE,
                              samples_md.LOCATION).filter_by(SAMPLEID = sample[3:]).all()
    result = {"age":md_query[3],
               "bb_type":md_query[4],
               "ethnicity":md_query[1], 
               "gender":md_query[2],
               "location":md_query[5],
               "sample_id":md_query[0]}
    return jsonify(result)

@app.route('/wfreq/<sample>')
def wfreq(sample):
    wash_query = session.query(samples_md.WFREQ).filter_by(SAMPLEID = sample[3:]).all()
    result = {"wfreq":wash_query[0][0]}
    return jsonify(result)

@app.route('/samples/<sample>')
def samples(sample):
    samples_query = session.query(samples.otu_id, "samples.{}".format(sample)).order_by(desc("samples.{}".format(sample))).all()
    result = [{"otu_ids":samples_query[i][0], "sample_values":samples_query[i][1]} for i in range(len(samples_query))]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)