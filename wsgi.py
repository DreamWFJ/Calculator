#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:         WFJ
Version:        0.1.0
FileName:       wsgi.py
CreateTime:     2017-05-06 22:50
"""
from app import create_app

application = create_app()

if __name__ == '__main__':
    application.run()