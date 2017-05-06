#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:         WFJ
Version:        0.1.0
FileName:       views.py
CreateTime:     2017-05-02 22:00
"""
import json
from flask import render_template, request
from ..import db
from . import main

@main.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/load-data', methods = ['GET','POST'])
def load_data():
    print "request.method: ",request.method
    print "request.form: ", request.form
    print "request.args: ",request.args
    return json.dumps({'result':"ok"})


@main.route('/calculate-loan', methods = ['POST'])
def calculate_loan():
    print request.form
    import time
    time.sleep(2)
    return json.dumps({'result':"ok"})


@main.route('/calculate-public-accumulation-funds-loan', methods = ['POST'])
def calculate_public_accumulation_funds_loan():
    print request.form
    import time
    time.sleep(2)
    return json.dumps({'result':"ok"})

@main.route('/calculate-prepayment', methods = ['POST'])
def calculate_prepayment():
    print request.form
    import time
    time.sleep(2)
    return json.dumps({'result':"ok"})

@main.route('/calculate-home-affordability', methods = ['POST'])
def calculate_home_affordability():
    print request.form
    import time
    time.sleep(2)
    return json.dumps({'result':"ok"})