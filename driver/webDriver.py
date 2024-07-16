from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException
import subprocess
import baixaDriver

dirAtual = Path(__file__).resolve().parent
dirPrincipal = dirAtual.parent
driverExe = dirPrincipal / 'chromeDriver' / 'chromedriver-win64' / 'chromedriver.exe'
userDataDir = dirPrincipal / 'chromeDriver' / 'user-data'


def obtem_versao_chromedriver():
    try:
        result = subprocess.run([str(driverExe), '--version'], capture_output=True, text=True)
        version = result.stdout.split(' ')[1]
        return version
    except Exception as e:
        print(f"Erro ao obter a versão do ChromeDriver: {e}")
        return None

# Função principal do WebDriver
def webDriver():
    versao_chromedriver = obtem_versao_chromedriver()
    if not versao_chromedriver:
        print("Não foi possível obter a versão do ChromeDriver.")
        return

    chrome_options = Options()
    chrome_options.add_argument(f'--user-data-dir={userDataDir}')
    # chrome_options.add_argument('--headless')
    chrome_service = Service(driverExe)

    try:
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get('https://example.com/')
        
    except SessionNotCreatedException as e:
        print(f"Erro ao inicializar o WebDriver: {e}")
        if "This version of ChromeDriver only supports Chrome version" in str(e):
            if baixaDriver():
                print("Nova versão do ChromeDriver baixada com sucesso. Tentando novamente.")
                webDriver()
            else:
                print("Não foi possível baixar uma versão compatível do ChromeDriver.")
        else:
            print("Erro inesperado ao tentar iniciar o WebDriver.")

# Testar o WebDriver
webDriver()
