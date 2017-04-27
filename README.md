# Coding dojo: Jogo - Adivinha o número

## Desafios
  ### Desafio 1 [:+1:]:

    - O bot deve gerar um número aleatório entre 1 e 100
    - A pessoa deve enviar palpites para tentar adivinhar o número
    - A cada palpite o bot deve dizer se está certo. Caso esteja errado, dizer se o palpite foi maior ou menor

  ### Desafio 2 [:+1:]:

    Limitar o número de tentativas para 10

  ### Desafio 3:

    Permitir jogar em um canal, ou seja, responder individualmente os palpites das pessoas mencionando os nomes delas

## Bot users
  ### Guia do Slack para bot users
    https://api.slack.com/bot-users
  ### Para adicionar um novo bot user
    https://<team domain>.slack.com/apps/manage/custom-integrations

  ### Real Time Messaging API
    https://api.slack.com/rtm
  ### Events API
    https://api.slack.com/events-api

## Requisitos:
  * ter o pyhton-2.7 instalado
  * ter o [virtualenv](https://virtualenv.pypa.io/en/stable/installation) instalado (para criar um ambiente isolado de desenvolvimento, assim, evita problemas com versões de dependências)

## Preparação do ambiente
  * criar um novo ambiente virtual:
  
  	*`$ virtualenv env`*
	
	*`$ source env/bin/activate`*

  * Instalar as dependências:
  
  	*`$ pip install -r requirements.txt`*

  * definir as variáveis de ambiente:
  
  	*SLACK_BOT_TOKEN: API Token fornecida ao configurar o bot no diretório do Slack*
	
	*BOT_ID: id de usuário do bot. Pode ser obtido através do script print_bot_id.py*
	
	>print_bot_id.py depende do SLACK_BOT_TOKEN, e do nome do bot que deve ser definido dentro do script

  * executar o script do bot
  
  	*`$ python bot.py`*

  * Seu bot está rodando local :)
  
## Fazendo o deploy no Heroku
	coming soon :)
