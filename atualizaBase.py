import requests
import xml.etree.ElementTree as et
import psycopg2
from datetime import datetime, timezone

def formatandoParaInsersao(cotacao):
    print(cotacao.values())
    v=cotacao.values()
    value = ""
    for moeda in v:
        value += "'" + moeda['codein'] + "'" + ","
        value += "'" + moeda['name'] + "'" + ","
        value += moeda['high'] + ","
        value += moeda['low'] +","
        value += moeda['pctChange'] + ","
        value += moeda['varBid'] + ","
        value += moeda['bid'] + ","
        value += moeda['ask'] + ","
        value += "to_timestamp(" +moeda['timestamp']+")"+ ","
        value += "'"+moeda['create_date'] + "'"+","
        value += "'" + str(datetime.now(timezone.utc)) + "'"
    return  value

listaDemoedasXML = requests.get('https://economia.awesomeapi.com.br/xml/available/uniq')
if (listaDemoedasXML.status_code != 200):
    print(listaDemoedasXML.status_code)
    exit(0)
print(listaDemoedasXML.text)
xml = et.fromstring(listaDemoedasXML.text)
listaDeMoedas = []
for elem in xml.iter():
    listaDeMoedas.append(elem.tag)
listaDeMoedas = list(set(listaDeMoedas))
print(listaDeMoedas)
conn = psycopg2.connect("host=localhost dbname=SBFTeste user=postgres password=h3rcul3s")
db = conn.cursor()
for moeda in listaDeMoedas:
    cotacao = requests.get('https://economia.awesomeapi.com.br/json/last/BRL-' + moeda)
    cotacao = cotacao.json()
   # print(cotacao)
    cotacao = dict(cotacao)
    if 'code' not in cotacao or cotacao['code'] != 'CoinNotExists':
        values = formatandoParaInsersao(cotacao)
        updateList=values.split(',')
        db.execute('insert into public.moedascotacao (code, "name", high, low, pctchange, varbid, bid, ask, "timestamp", dateofcotation, lastupdate) values('+values+')\
                  on conflict(code) do update set code='+updateList[0]+', "name"='+updateList[1]+', high='+updateList[2]+', low='+updateList[3]+\
                   ', pctchange='+updateList[4]+', varbid='+updateList[5]+', bid='+updateList[6]+', ask='+updateList[7]+', "timestamp"='+updateList[8]+',lastupdate='+updateList[9])

conn.commit()

