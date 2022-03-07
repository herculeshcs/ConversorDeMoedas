# SBFTeste
# Como a API funciona:
1. Ela consome a cada 30 minutos (atualizaBase.py) https://economia.awesomeapi.com.br para atualizar uma tabela com as cotações de todas as cerca de 60 moedas disponiveis.
2. Isso é feito dentro do conteiner onde gravamos os dados em um banco postgres.
3. Quando se faz uma requisição outro programa escrito em python usando flask(app.py) consome essa tabela para determinar realizar a conversao.

# Instalando API 

## Basta executar o script installAPI.sh

### Você também pode executar a seguencia de comandos abaixo :

   1.**docker pull hercules42/sbfteste:latest** 

   2.**sudo docker run --name testeSBF -p 8080:8080 -d -it hercules42/sbfteste /bin/bash**

   3.**docker exec testeSBF service postgresql start**

   4.**docker exec testeSBF waitress-serve --port=8080 --call app:create_app**


# Usando a API:

um get para o seguinte endereço retorna o Valor em reai convertido para a Moeda Representada pelo Simbol

convertCurrency?currency=Simbolo&realValue=Valor

| Parametro       | Type     | Obrigatorio?  | descrição                                                                                                 |
| -------------   |----------|---------------|-----------------------------------------------------------------------------------------------------------|
| `currency`      | string   | sim           | Simbolo da Moeda a ser convertida, pode-se consultar quais os simbolos usando o serviço: getAllCurrency
| 'realValue'     | decimal  | sim           | Preço em reais que será convertido.

Resposta:

{"valorConvertido": string, "tipoConversao": string, "fatorConversao": String}


####Onde:

  -valorConvertid = Valor convertido para a moeda alvo.
  
  
  -tipoConversao  = Vai informar qual a conversão foi feita, sempre BRL-Simbolo, onde Simbolo é o simbolo usado para representar outra moeda.
  
  
  -fatorConversao = Vai informar qual o fator usada na conversão onde valorConvertido=realValue*fator
  
 Exemplo:
 

 http://127.0.0.1:5000/convertCurrency?currency=USD&realValue=10
 deve responder
 
 {"valorConvertido": "1.990", "tipoConversao": "BRL-USD", "fatorConversao": "0.199"}
 
 
 A resposta da API varia já que as cotações são atualizadas a cada 30 minutos.

# Moedas Suportadas e seus símbolos:

|Símbolo|Conversao de/para                       |
|-------|----------------------------------------|
|XOF    |Real Brasileiro/Franco CFA Ocidental    |
|LKR    |Real Brasileiro/Rúpia de Sri Lanka      |
|ARS    |Real Brasileiro/Peso Argentino          |
|PEN    |Real Brasileiro/Sol do Peru             |
|BBD    |Real Brasileiro/Dólar de Barbados       |
|PKR    |Real Brasileiro/Rúpia Paquistanesa      |
|LBP    |Real Brasileiro/Libra Libanesa          |
|PYG    |Real Brasileiro/Guarani Paraguaio       |
|ILS    |Real Brasileiro/Novo Shekel Israelense  |
|NPR    |Real Brasileiro/Rúpia Nepalesa          |
|CNY    |Real Brasileiro/Yuan Chinês             |
|COP    |Real Brasileiro/Peso Colombiano         |
|PHP    |Real Brasileiro/Peso Filipino           |
|KES    |Real Brasileiro/Shilling Queniano       |
|BHD    |Real Brasileiro/Dinar do Bahrein        |
|DKK    |Real Brasileiro/Coroa Dinamarquesa      |
|ZAR    |Real Brasileiro/Rand Sul-Africano       |
|ISK    |Real Brasileiro/Coroa Islandesa         |
|MYR    |Real Brasileiro/Ringgit Malaio          |
|TRY    |Real Brasileiro/Nova Lira Turca         |
|CAD    |Real Brasileiro/Dólar Canadense         |
|VEF    |Real Brasileiro/Bolívar Venezuelano     |
|RON    |Real Brasileiro/Leu Romeno              |
|BRLT   |Dólar Americano/Real Brasileiro Turismo |
|EUR    |Real Brasileiro/Euro                    |
|USD    |Real Brasileiro/Dólar Americano         |
|UYU    |Real Brasileiro/Peso Uruguaio           |
|JOD    |Real Brasileiro/Dinar Jordaniano        |
|JMD    |Real Brasileiro/Dólar Jamaicano         |
|HKD    |Real Brasileiro/Dólar de Hong Kong      |
|AED    |Real Brasileiro/Dirham dos Emirados     |
|BOB    |Real Brasileiro/Boliviano               |
|THB    |Real Brasileiro/Baht Tailandês          |
|CHF    |Real Brasileiro/Franco Suíço            |
|SAR    |Real Brasileiro/Riyal Saudita           |
|NZD    |Real Brasileiro/Dólar Neozelandês       |
|QAR    |Real Brasileiro/Rial Catarense          |
|XCD    |Real Brasileiro/Dólar do Caribe Oriental|
|SGD    |Real Brasileiro/Dólar de Cingapura      |
|NAD    |Real Brasileiro/Dólar Namíbio           |
|NOK    |Real Brasileiro/Coroa Norueguesa        |
|INR    |Real Brasileiro/Rúpia Indiana           |
|PLN    |Real Brasileiro/Zlóti Polonês           |
|RUB    |Real Brasileiro/Rublo Russo             |
|AUD    |Real Brasileiro/Dólar Australiano       |
|XAF    |Real Brasileiro/Franco CFA Central      |
|KRW    |Real Brasileiro/Won Sul-Coreano         |
|EGP    |Real Brasileiro/Libra Egípcia           |
|HUF    |Real Brasileiro/Florim Húngaro          |
|CLP    |Real Brasileiro/Peso Chileno            |
|CZK    |Real Brasileiro/Coroa Checa             |
|JPY    |Real Brasileiro/Iene Japonês            |
|MAD    |Real Brasileiro/Dirham Marroquino       |
|OMR    |Real Brasileiro/Rial Omanense           |
|IDR    |Real Brasileiro/Rupia Indonésia         |
|MXN    |Real Brasileiro/Peso Mexicano           |
|SEK    |Real Brasileiro/Coroa Sueca             |
|PAB    |Real Brasileiro/Balboa Panamenho        |
|TWD    |Real Brasileiro/Dólar Taiuanês          |
|GBP    |Real Brasileiro/Libra Esterlina         |


