# -*- coding: utf-8 -*-
# ===================================
# ScriptName : tr_update.py
# Author     : WFJ
# Email      : wfj_sc@163.com
# CreateTime : 2017-05-08 9:17
# ===================================

import os

os.system('pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot app')
os.system('pybabel update -i messages.pot -d app/translations')
os.unlink('messages.pot')