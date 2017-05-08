#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:         WFJ
Version:        0.1.0
FileName:       views.py
CreateTime:     2017-05-02 22:00
"""

from . import main
from app import babel
from config import LANGUAGES
from flask_babel import gettext,_
from flask import render_template, request, jsonify

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())


@main.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/load-data', methods = ['GET','POST'])
def load_data():
    print "request.method: ",request.method
    print "request.form: ", request.form
    print "request.args: ",request.args
    return jsonify({'result':"ok"})


@main.route('/calculate-loan', methods = ['POST'])
def calculate_loan():
    print request.form
    """
    每月月供额=〔贷款本金×月利率×(1＋月利率)＾还款月数〕÷〔(1＋月利率)＾还款月数-1〕
    每月应还利息=贷款本金×月利率×〔(1+月利率)^还款月数-(1+月利率)^(还款月序号-1)〕÷〔(1+月利率)^还款月数-1〕
    每月应还本金=贷款本金×月利率×(1+月利率)^(还款月序号-1)÷〔(1+月利率)^还款月数-1〕
    总利息=还款月数×每月月供额-贷款本金
    """
    loan_type =  request.form.get('loan-type')
    print "loan type: ", loan_type
    compute_mode =  request.form.get('compute-mode')
    if compute_mode == "on":
        # area_price
        total_area = request.form.get('total-area')
        unit_price = request.form.get('unit-price')
        mortgage_percentage = request.form.get('mortgage-percentage')
        total_loan = float(total_area) * float(unit_price) * float(mortgage_percentage)
    else:
        # total_loan
        total_loan = float(request.form.get('total-loan'))
    print "total loan: ", total_loan
    mortgage_year = float(request.form.get('mortgage-year'))
    loan_rate = float(request.form.get('loan-rate'))
    repayment_mode = request.form.get('repayment-mode')



    if repayment_mode == 'on':
        # 等额本息还款法 Fixed-payment Mortgage
        # 每月月供额
        monthly_payment_loans = (total_loan * loan_rate * (1+loan_rate)**(mortgage_year * 12))/((1+loan_rate)**(mortgage_year * 12) - 1)
        monthly_payment_interests = total_loan * loan_rate * ((1+loan_rate)**(mortgage_year * 12) - (1+loan_rate)**(mortgage_year * 12 - 1)) / ((1+loan_rate)**(mortgage_year * 12) - 1)
        monthly_payment_principals = total_loan * loan_rate * (1+loan_rate)**(mortgage_year * 12 - 1) / ((1+loan_rate)**(mortgage_year * 12) - 1)
        total_interests = (mortgage_year * 12) * monthly_payment_loans - total_loan
        print "Monthly payments: ",monthly_payment_loans
        print "monthly_payment_interests: ",monthly_payment_interests
        print "monthly_payment_principals: ",monthly_payment_principals
        print "total_interests: ",total_interests
    else:
        # 等额本金还款法 Fixed-basis Mortgage
        pass

    return jsonify({'result':{
        "home_total_price":123,
        "home_total_loan":124,
        "repayment_total_price":1233,
        "payment_interest":231,
        "first_payment":311,
        "loan_terms":12,
        "average_monthly_repayment":132
    }})


@main.route('/calculate-public-accumulation-funds-loan', methods = ['POST'])
def calculate_public_accumulation_funds_loan():
    print request.form
    import time
    time.sleep(2)
    return jsonify({'result':_("ok")})

@main.route('/calculate-prepayment', methods = ['POST'])
def calculate_prepayment():
    print request.form
    import time
    time.sleep(2)
    return jsonify({'result':"ok"})

@main.route('/calculate-home-affordability', methods = ['POST'])
def calculate_home_affordability():
    print request.form
    import time
    time.sleep(2)
    return jsonify({'result':"ok"})