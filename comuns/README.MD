<h1> Complementos sobre COMUNS </h1>

<h3> COMUNS é um complemento dos arquivos de task </h3>

<p>- Variaveis de ambiente<br>
- Configurações<br>
- Notificações no slack</p>

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
