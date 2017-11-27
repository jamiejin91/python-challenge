from flask import Flask, jsonify, render_template, redirect

import scrape_mars


app = Flask(__name__)