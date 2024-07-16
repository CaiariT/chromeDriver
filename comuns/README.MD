## -notification_slack.py
Esse aquivo chama a função de enviar notificações em um canal especifico do Slack. 


Ao importar o arquivo:
```http
from comuns.notification_slack import send_notification, notify_slack_error
```

Chame a seguinte variavel passando o dado que sera enviado no slack:

```http
send_notification("Olá, Slack! Esta é uma mensagem de teste.")
```

```http
notify_slack_error("Ocorreu um erro no sistema!")
```
