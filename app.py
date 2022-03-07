# -*- coding: utf-8 -*-
import json

from flask import Flask
from flask import request
from decimal import Decimal

import psycopg2
import psycopg2.extras

app = Flask(__name__)


@app.route("/convertCurrency", methods=['GET'])
def converCurrency():
    try:
        currencyTarget = request.args.get("currency")
        realValue = request.args.get("realValue")
        if (currencyTarget is None):
            return "não informado a moeda para conversão"
        if (realValue is None):
            return "defina um valor em reais"
        conn = psycopg2.connect("host=localhost dbname=SBFTeste user=postgres password=h3rcul3s")
        curDb = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        curDb.execute("select * from public.moedascotacao where code='" + currencyTarget + "'")
        data = curDb.fetchone()
        convertFactor = data['high']
        convertValue = dict()
        convertValue['valorConvertido'] = str(Decimal(realValue) * convertFactor)
        convertValue['tipoConversao'] ="BRL-"+currencyTarget
        convertValue['fatorConversao'] = str(data['high'])
        return json.dumps(convertValue)
    except Exception as error:
        return str(error)

@app.route("/getAllCurrency", methods=['GET'])
def getAllCurrency():
    try:
        conn = psycopg2.connect("host=localhost dbname=SBFTeste user=postgres password=h3rcul3s")
        curDb = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        curDb.execute("select code,\"name\" from public.moedascotacao")
        data = curDb.fetchall()
        return json.dumps(data)
    except Exception as error:
            return str(error)
app.run()
