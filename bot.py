#coding: utf-8

import os
import time
import random
import json
from slackclient import SlackClient


BOT_ID = os.environ.get("BOT_ID")
BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
base_url = "https://slack.com"
AT_BOT = "<@" + BOT_ID + ">"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
segredo = 0
qtdTentativa = 0

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text'] and 'user' in output:
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel'], output['user']
    return None, None

def handle_command(command, channel, user):
    global qtdTentativa
    global segredo
    if command == "start":
        qtdTentativa = 0
        segredo = random.randint(0,100)
        response = "Adivinhe o número de 0 a 100"
    elif command.isdigit():
        if qtdTentativa > 2:
            response = "Acabaram suas tentativas."
        else:
            qtdTentativa = qtdTentativa + 1
            tentativa = int(command)
            if tentativa > segredo:
                response = "Ops, seu número foi alto!"
            elif tentativa == segredo:
                response = "Parabens!!!"
            else:
                response = "Ops, seu número foi baixo!"
    else:
        response = "Desculpe, infelizmente ainda não faço muita coisa."
    
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("dojo-boy connected and running!")
        while True:
            info = parse_slack_output(slack_client.rtm_read())
            if len(info) == 3:
                command = info[0]
                channel = info[1]
                user = info[2]
                handle_command(command, channel, user)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
