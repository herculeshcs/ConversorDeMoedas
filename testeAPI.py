import requests


configFile = open('teste.conf', 'r')

lines = configFile.readlines()

host=lines[0]
host=host.replace("\n","")
currencylist=lines[1].split(",")
total =0
fails=0
win=0
for currency in currencylist:
    total=total+1
    currency=currency.replace("\"","")
    request = host + "/convertCurrency?" + "currency" + "=" + currency + "&" + "realValue=10"
    response=requests.get(request)
    if(response.status_code!=200):
        print("falha no teste para a requisição " +request)
        print("codigo de erro http = "+str(response.status_code))
        fails = fails + 1
    else:
        print("Requisição:"+ request +" Devolveu :" )
        print(response.json())
        win = win + 1


print("total de testes= "+str(total))
print("numero de sucessos= "+str(win))
print("numero de falhas= "+str(fails))