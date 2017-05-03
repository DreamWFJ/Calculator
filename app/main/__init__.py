#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:         WFJ
Version:        0.1.0
FileName:       __init__.py.py
CreateTime:     2017-05-02 21:47
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views