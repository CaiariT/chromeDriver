from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import os
from dotenv import load_dotenv
load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
SLACK_CHANNEL_DENEGADA = os.getenv("SLACK_CHANNEL_DENEGADA")
client = WebClient(token=SLACK_TOKEN)


def send_notification(message):
    try:
        client = WebClient(token=SLACK_TOKEN)
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=message
        )
        print("Mensagem de inicialização enviada com sucesso:", response["message"]["text"])
    except SlackApiError as e:
        print("Erro ao enviar mensagem de inicialização:", e)



def notify_slack_error(error_message):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=SLACK_CHANNEL, text=error_message)
    except SlackApiError as e:
        print(f"Erro ao enviar a mensagem para o Slack: {e.response['error']}")



def notify_slack_error(error_message):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=SLACK_CHANNEL, text=error_message)
    except SlackApiError as e:
        print(f"Erro ao enviar a mensagem para o Slack: {e.response['error']}")
#example
#send_notification("Olá, Slack! Esta é uma mensagem de teste.")
        
#example
#notify_slack_error("Ocorreu um erro no sistema!")