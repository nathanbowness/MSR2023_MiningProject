# API-3.0-Python

SDK API-3.0 Python Cielo



* [Principais recursos](#principais-recursos)
* [Limitações](#limitações)
* [Instalação](#instalação)
* [Exemplos](#exemplos)
    * [Criando um pagamento com cartão de crédito](#criando-um-pagamento-com-cartão-de-crédito)
    * [Criando um pagamento recursivo com cartão de crédito](#criando-um-pagamento-recursivo-com-cartão-de-crédito)
    * [Criando um agendamento de pagamento recursivo com cartão de crédito](#criando-um-agendamento-de-pagamento-recursivo-com-cartão-de-crédito)
    * [Gerando token de cartão de crédito e criando um pagamento com o token](#gerando-token-de-cartão-de-crédito-e-criando-um-pagamento-com-o-token)
    * [Gerando um boleto simples](#gerando-um-boleto-simples)
    * [Gerando um boleto completo](#gerando-um-boleto-completo)
* [Manual Oficial da Cielo](#manual-oficial-da-cielo)

## Principais recursos

* [x] Pagamentos por cartão de crédito.
* [x] Pagamentos recorrentes.
    * [x] Com autorização na primeira recorrência.
    * [x] Com autorização a partir da primeira recorrência.
* [x] Pagamentos por cartão de débito.
* [x] Pagamentos por boleto (Bradesco e Banco do Brasil).
* [ ] Pagamentos por transferência eletrônica.
* [x] Cancelamento de autorização.
* [x] Consulta de pagamentos.

## Limitações

Por envolver a interface de usuário da aplicação, o SDK funciona apenas como um framework para criação das transações. Nos casos onde a autorização é direta, não há limitação; mas nos casos onde é necessário a autenticação ou qualquer tipo de redirecionamento do usuário, o desenvolvedor deverá utilizar o SDK para gerar o pagamento e, com o link retornado pela Cielo, providenciar o redirecionamento do usuário.

## Instalação
O API-3.0 Python Cielo pode ser facilmente instalado com o comando a seguir:
```bash
pip install cieloApi3
```

## Exemplos
### Criando um pagamento com cartão de crédito

```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('123')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Fulano de Tal')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '0000000000000001'
credit_card.holder = 'Fulano de Tal'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(15700)
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer sua captura,
# se ela não tiver sido capturada ainda
response_capture_sale = cielo_ecommerce.capture_sale(payment_id, 15700, 0)
print '----------------------response_capture_sale----------------------'
print json.dumps(response_capture_sale, indent=2)
print '----------------------response_capture_sale----------------------'

# E também podemos fazer seu cancelamento, se for o caso
response_cancel_sale = cielo_ecommerce.cancel_sale(payment_id, 15700)
print '---------------------response_cancel_sale---------------------'
print json.dumps(response_cancel_sale, indent=2)
print '---------------------response_cancel_sale---------------------'
```


### Criando um pagamento recursivo com cartão de crédito
```python

from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('789')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador accept')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('262', 'Visa')
credit_card.expiration_date = '03/2019'
credit_card.card_number = '1234123412341231'
credit_card.holder = 'Teste Holder'

recurrent_payment = RecurrentPayment()
recurrent_payment.interval = INTERVAL_SEMIANNUAL
recurrent_payment.end_date = '2019-12-01'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(1500)
sale.payment.recurrent_payment = recurrent_payment
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'



# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer sua captura,
# se ela não tiver sido capturada ainda
response_capture_sale = cielo_ecommerce.capture_sale(payment_id, 15700, 0)
print '----------------------response_capture_sale----------------------'
print json.dumps(response_capture_sale, indent=2)
print '----------------------response_capture_sale----------------------'

# E também podemos fazer seu cancelamento, se for o caso
response_cancel_sale = cielo_ecommerce.cancel_sale(payment_id, 15700)
print '---------------------response_cancel_sale---------------------'
print json.dumps(response_cancel_sale, indent=2)
print '---------------------response_cancel_sale---------------------'



# Com a venda recorrente criada na Cielo, já temos o ID do pagamento recorrente
recurrent_payment_id = sale.payment.recurrent_payment.recurrent_payment_id

# Consulta informações da venda recorrente
response_get_recurrent_payment = cielo_ecommerce.get_recurrent_payment(recurrent_payment_id)
print '---------------------response_get_recurrent_payment---------------------'
print json.dumps(response_get_recurrent_payment, indent=2)
print '---------------------response_get_recurrent_payment---------------------'
```


### Criando um agendamento de pagamento recursivo com cartão de crédito
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('789')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador rec programada')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('262', 'Visa')
credit_card.expiration_date = '03/2019'
credit_card.card_number = '1234123412341231'
credit_card.holder = 'Teste Holder'

recurrent_payment = RecurrentPayment(False)
recurrent_payment.interval = INTERVAL_SEMIANNUAL
recurrent_payment.start_date = '2015-06-01'
recurrent_payment.end_date = '2019-12-01'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(1500)
sale.payment.recurrent_payment = recurrent_payment
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'
```

### Gerando token de cartão de crédito e criando um pagamento com o token
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '4532117080573700'
credit_card.holder = 'Comprador T Cielo'
credit_card.customer_name = 'Comprador Teste Cielo'

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_card_token = cielo_ecommerce.create_card_token(credit_card)
print '----------------------response_create_card_token----------------------'
print json.dumps(response_create_card_token, indent=2)
print '----------------------response_create_card_token----------------------'

# Com o cartão gerado token na Cielo, já temos o Token do cartão para uma futura cobrança
new_card_token = credit_card.card_token
print 'New Card Token:', new_card_token

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('456')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Credit Card utilizando os dados de teste via token
credit_card_token = CreditCard('123', 'Visa')
credit_card_token.card_token = new_card_token

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(100)
sale.payment.credit_card = credit_card_token

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'
```

### Gerando um boleto simples
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('333')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(15700)
sale.payment.type = PAYMENTTYPE_BOLETO

sale.payment.provider = PROVIDER_BRADESCO

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer uma consulta do pagamento
response_get_sale = cielo_ecommerce.get_sale(payment_id)
print '----------------------response_get_sale----------------------'
print json.dumps(response_get_sale, indent=2)
print '----------------------response_get_sale----------------------'

print '\r\nLink Boleto:', sale.payment.url, '\r\n'
```

### Gerando um boleto completo
```python
from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('555')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Payment informando o valor do pagamento
payment = Payment(15700)
payment.type = PAYMENTTYPE_BOLETO

payment.provider = PROVIDER_BANCO_DO_BRASIL
payment.address = 'Rua Alegria N: 3 Bairro: Rosa São Paulo-SP'
payment.boleto_number = '123'
payment.assignor = 'Empresa Teste'
payment.demonstrative = 'Demonstrativo Teste'
payment.expiration_date = '2017-06-11'
payment.identification = '11884926754'
payment.instructions = 'Aceitar somente até a data de vencimento, após essa data juros de 1% dia.'

sale.payment = payment

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print '----------------------response_create_sale----------------------'
print json.dumps(response_create_sale, indent=2)
print '----------------------response_create_sale----------------------'

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer uma consulta do pagamento
response_get_sale = cielo_ecommerce.get_sale(payment_id)
print '----------------------response_get_sale----------------------'
print json.dumps(response_get_sale, indent=2)
print '----------------------response_get_sale----------------------'

print '\r\nLink Boleto:', sale.payment.url, '\r\n'
```

## Manual Oficial da Cielo

Para mais informações sobre a integração com a API 3.0 da Cielo, vide o manual em: [Integração API 3.0](https://developercielo.github.io/Webservice-3.0/)
