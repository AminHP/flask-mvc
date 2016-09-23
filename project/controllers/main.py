# -*- coding: utf-8 -*-

# project imports
from project import app

# flask imports
from flask import render_template, request, jsonify


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>')
def home(name):
    return render_template('home.html', name=name)


@app.route('/', methods=['POST'])
@app.validate('main.welcome')
def welcome():
    return jsonify(name=request.json['name'])
