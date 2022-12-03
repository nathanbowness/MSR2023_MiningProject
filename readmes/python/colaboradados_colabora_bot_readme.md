# Colaborabot

### O robô criado pelo [Colaboradados](https://colaboradados.com.br/) para monitorar o acesso aos portais de transparência pública governamentais.


<a href="https://twitter.com/colaboradados"> <img src="colaboradados_twitter_logo.png" width="200"></a>

Este repositório se refere ao nosso bot que monitora portais de transparência pública governamentais. Acesse e siga [**aqui**](https://twitter.com/colabora_bot).

## Stack

- [Python3][https://www.python.org/] a linguagem de programação necessária para executar o bot.
- [Virtualenv][https://docs.python-guide.org/dev/virtualenvs/] um ambiente virtual para isolar os pacotes que serão instalados com o bot.

## Instalando o bot

### Executar localmente

1. Fork o [repositório](https://github.com/colaboradados/colabora_bot) para o seu Github.
2. Clone o repositório digitando `$ git clone https://github.com/<seu_usuario>/colabora_bot.git` no Terminal.
3. Ative seu ambiente virtual e entre na pasta raíz do bot.
4. Crie um arquivo na raiz do projeto chamado `.env`, que será utilizado para salvar as variáveis de configuração do bot, como tokens.
5. Copie o conteúdo do arquivo `.env.example` para o arquivo recém criado `.env`.
> Note que este arquivo de exemplo contem a variavel `DEBUG=True`, isso irá desativar as dependencias externas do bot para rodar localmente sem problemas.
6. Instale as dependências necessárias com `pip install -r requirements.txt`.
7. Para rodar o bot, execute `python colaborabot.py`.
8. Pronto, agora é só executar e contribuir!

### Configurando dependências externas e tokens
Para mais detalhes sobre as dependencias externas acesse [o arquivo de integrações aqui](/docs/INTEGRACOES.md).

### Colaborando com o robô (e sendo uma pessoa muito legal)

O **Colaboradados** é uma iniciativa sem fins lucrativos e feita para a comunidade e com a ajuda da mesma. Para ajudar com nossa base de dados você poderá resolver nossas issues ou editando diretamente nosso arquivo [`lista_portais.csv`](/dados/lista_portais.csv).

Atente-se ao fato de que nosso programa foi criado pensando no escopo nacional brasileiro, portanto seu código é - deverá ser - sempre em português, onde possível. Evite estrangeirismos e colabore para que nosso código seja estudado por todas as pessoas interessadas em transparência.

Nosso projeto é uma porta de entrada para que pessoas das mais diversas áreas do conhecimento se interessem com o processo tecno-cívico participativo, portanto acreditamos que o robô deve ser de fácil entendimento para aqueles que não possuem tanta familiaridade com técnicas mais avançadas de programação.

_Simples é melhor que complexo_

_Complexo é melhor que complicado_

## Créditos

Este bot foi desenvolvido por [João Ernane](https://github.com/jovemadulto), [João Purger](https://github.com/JCPurger) e [Judite Cypreste](https://juditecypreste.github.io).

## The MIT License (MIT)

### Português (tradução livre)

Copyright (c) 2019 Judite Cypreste

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e dos arquivos de documentação associados (o "Software"), para lidar com o software sem restrições, incluindo, sem limitação, os direitos de uso, cópia, modificação, merge, publicar, distribuir, sublicenciar e / ou vender cópias do Software e permitir que as pessoas a quem o software é fornecido o façam, sob as seguintes condições:

A declaração de direitos autorais acima e esta permissão devem ser incluídos em todas as cópias ou partes substanciais do software.

O SOFTWARE É FORNECIDO "TAL COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO MAS NÃO SE LIMITANDO A GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA E NÃO INFRACÇÃO. EM NENHUM CASO OS AUTORES OU TITULARES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER REIVINDICAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, TORT OU OUTRA FORMA, DECORRENTE DE, FORA DE OU RELACIONADO AO SOFTWARE OU O USO DE PROUTOS.

### Inglês (original)

Copyright (c) 2019 Judite Cypreste

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
