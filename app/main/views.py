#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:         WFJ
Version:        0.1.0
FileName:       views.py
CreateTime:     2017-05-02 22:00
"""
from flask import render_template
from ..import db
from . import main

@main.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')