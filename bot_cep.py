# -*- coding: utf-8 -*-

import requests
import json
import telepot
import random
import re
import sys
import time
# Bot Para consultar CEP e IBGE com Telegram API
# Modo de uso: /cep 04320-040
# Developers:
# Jonatas FIL a.k.a Dkr and Tesla

reload(sys)
sys.setdefaultencoding('utf8')

def handle(msg):
    tipomsg, tipochat, chat_id = telepot.glance(msg)
    #print(msg)

    command = msg['text'].split(' ')
    if command[0] == '/cep':
        cep = command[1]
        api = "https://viacep.com.br/ws/"+cep+"/json/unicode/" # API JSON

        r = requests.get(api)
        results = json.loads(r.content)
        print(results)

        txt = 'Consulta de CEP e IBGE no Telegram:\n{Criado por Dkr e Tesla.}\n\nCep: '+results['cep']+'\nLogradouro: '+results['logradouro']+'\nComplemento: '+results['complemento']+'\nBairro: '+results['bairro']+'\nLocalidade: '+results['localidade']+'\nUF: '+results['uf']+'\nIBGE: '+results['ibge']
        bot.sendMessage(chat_id, txt) # Envia O resultado

TOKEN = ''

bot = telepot.Bot('') # SUA API AQUI
bot.message_loop(handle)
print ('Aguarde...')
print ('Modo de uso: /cep 04320-040')

while 1:
    time.sleep(10)
