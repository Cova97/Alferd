from flask import Flask, render_template, jsonify, request, send_file
from marshmallow import SchemaOpts, Schema

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
