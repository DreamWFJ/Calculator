#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:         WFJ
Version:        0.1.0
FileName:       config.py
CreateTime:     2017-05-02 21:57
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLACHEMY_RECORD_QUERIES = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite').replace('\\', '/')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass