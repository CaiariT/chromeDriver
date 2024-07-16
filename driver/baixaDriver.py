import requests
import os
import zipfile
import io
from pathlib import Path



dirAtual = Path(__file__).resolve().parent
dirPrincipal = dirAtual.parent
driverArq = dirPrincipal / 'chromeDriver' / 'webDriver'


# Consulta a ultima versão do chromedriver:
version_url = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json'


def baixar_e_descompactar_arquivo(url, diretorio_destino):
    response = requests.get(url)
    if response.status_code == 200:
        
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:

            zip_ref.extractall(diretorio_destino)
            print(f"Arquivo baixado e descompactado em {diretorio_destino}")
    else:
        print(f"Erro ao baixar arquivo: {response.status_code} - {response.reason}")

try:
    response = requests.get(version_url)
    response.raise_for_status()  

    jsonData = response.json()

    if 'Stable' in jsonData['channels']:
        versao_atual = jsonData['channels']['Stable']['version']
        print('Versão estável:', versao_atual)

        url_completa = f'https://storage.googleapis.com/chrome-for-testing-public/{versao_atual}/win64/chromedriver-win64.zip'
        print('URL completa:', url_completa)


        dir_path = os.path.join(os.path.dirname(driverArq))
        print(dir_path)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print('Pasta "docs" criada com sucesso.')

        # Baixa e descompacta o arquivo
        baixar_e_descompactar_arquivo(url_completa, dir_path)
    else:
        print('Não existe versão estável disponível.')

except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer solicitação HTTP: {e}")
except Exception as e:
    print(f"Erro: {e}")
