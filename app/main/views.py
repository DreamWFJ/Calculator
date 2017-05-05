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

@main.route('/calculate-loan', methods = ['POST'])
def calculate_loan():
    print request.form
    import time
    time.sleep(2)
    return json.dumps({'result':"ok"})