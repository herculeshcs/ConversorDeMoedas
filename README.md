# SBFTeste

Usando a API:

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
 
---
 http://127.0.0.1:5000/convertCurrency?currency=USD&realValue=10

```
 deve responder
 ---
 {"valorConvertido": "1.990", "tipoConversao": "BRL-USD", "fatorConversao": "0.199"}
 A resposta da API varia já que as cotações são atualizadas a cada 30 minutos.

```


