#!/usr/bin/env bash
nohup gunicorn -w 4 -b 127.0.0.1:5000 wsgi:application >/dev/null 2>&1 &