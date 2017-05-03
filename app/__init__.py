#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:         WFJ
Version:        0.1.0
FileName:       __init__.py.py
CreateTime:     2017-05-02 21:02
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app