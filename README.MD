

# SERVICES CHROME DRIVER 
## Descrição do Serviço

Este script em Python foi desenvolvido para facilitar o uso do WebDriver com o navegador Chrome, sem a preocupação de baixar e manter manualmente a versão mais recente do ChromeDriver. O script verifica automaticamente a versão estável mais recente do ChromeDriver, baixa e descompacta o driver, e inicializa um novo navegador em branco. Isso garante que o WebDriver esteja sempre atualizado e pronto para uso.


## DESENVOLVIMENTO
Ferramenta utilizada para raspagem, inserção e atualização de dados, automações de processos em paginas web, onde não é possivel realizar com auxilios de APIs.

## NOTA TECNICA
#### Arquivos:
```webDriver.py``` -> É responsavel por instanciar, configurar e verificar atualizações da versão do navegador.

```dowsDriver``` -> recebe a Informação do webDriver e consulta a nova versão do navegador.

## Depois de instalar o Python, siga estas etapas:

1. git clone ```https://github.com/CaiariT/chromeDriver.git``` (clonar o repositório).
2. ```python3 -m venv myenv``` (criar um ambiente virtual).
3. ```source myenv\Scripts\activate)``` (ativar o ambiente virtual).
4. ```pip install -r requirements.txt``` (instalar as dependências).
Obs: caso quiser desativar a variavel de ambiente ```deactivate```.

### uso
em task/main.py é onde vai ser a parte principal do seu codigo, onde é chamada a função ```driver = webDriver()```, que baixa o navegador na pasta chromedriver e inicializa ele.



### CONFIS PARA NOTIFICAÇÕES NO SLACK:
Quando importada e chamada a função:
```python3
send_notification("Sua mensagem aqui")
```
ele envia para o canal escolhido o que voce desejar, basta configurar um App no Slack. 
```http
https://github.com/CaiariT/chromeDriver/blob/main/comuns/README.MD
```

## Obs
Na pasta driver em `webDriver.py` voce terá as chrome_opitions que basicamente salva a data | cache da pagina e utiliza novamente:
```Python3
chrome_options.add_argument(f'--user-data-dir={userDataDir}')
```
E aqui você configura para a tela do chome aparecer aberta, mostrando o conteudo, ou fazer o processo por baixo dos panos:
```Python3
chrome_options.add_argument('--headless')`
```
