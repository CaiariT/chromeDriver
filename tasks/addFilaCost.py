import requests
import os
import sys
import pymysql
import time
from bs4 import BeautifulSoup
import json
from decimal import Decimal

from datetime import date, datetime, timedelta

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_dir)

from comuns.notification_slack import send_notification, notify_slack_error
from driver.webDriver import webDriver

from dotenv import load_dotenv
load_dotenv()

db_host = os.getenv("")
db_user = os.getenv("")
db_password = os.getenv("")
db_name = os.getenv("")

connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
)

link_product = 'https://erp.tiny.com.br/produtos#edit/'
        
def verificaExistencia(cursor, dados, id_produto, chave_primaria):
    for dado in dados:
        data_custo = dado[1]
        preco_custo = str(dado[2])
        
        if '.' in preco_custo and len(preco_custo.split('.')[1]) > 4:
            preco_custo = "{:.4f}".format(float(preco_custo))
        preco_custo = Decimal(preco_custo)

        resultado = existe(cursor, id_produto, data_custo, preco_custo)

        if not resultado:
            inserirDados(cursor, dado, chave_primaria)
            remove_fila(id_produto, cursor, connection)
        else:
            remove_fila(id_produto, cursor, connection)
            
            
def coletarDados(driver, id):
    url = f'https://erp.tiny.com.br/produtos#edit/{id}'
    driver.get(url)
    time.sleep(4)
    
    html = driver.page_source    
    soup = BeautifulSoup(html, 'html.parser')
    historico_precos = soup.find(id='lista-historico-preco-custo')
    
    dados = []
    for linha in historico_precos.find_all('tr'):
        colunas = linha.find_all('td')
        if len(colunas) > 0:
            data_texto = colunas[0].find('p', class_='viewing-input').text.strip()
            data_objeto = datetime.strptime(data_texto, "%d/%m/%Y")
            data_formatada = data_objeto.strftime("%Y-%m-%d")
            
            preco_custo_texto = colunas[4].find('p', class_='viewing-input').text.strip().replace('.', '').replace(',', '.')
            custo_medio_texto = colunas[5].find('p', class_='viewing-input').text.strip().replace('.', '').replace(',', '.')
            
            preco_custo = Decimal(preco_custo_texto)
            custo_medio = Decimal(custo_medio_texto)
            
            dados.append((id, data_formatada, preco_custo, custo_medio))
            
    return dados


def process_filial(cnpj, name, sigla, email, senha):
    resultados, cursor = consultaItems(sigla)
    if resultados:  
        driver = webDriver(email, senha)
        
        for resultado in resultados: 
            id_produto, filial, data_emissao, chave_primaria = resultado.values()
            print(id_produto, chave_primaria)
            dados = coletarDados(driver, id_produto)
            verificaExistencia(cursor, dados, id_produto, chave_primaria)

        driver.quit()


def nfeWKI():
    process_filial(
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" ")
    )

def nfeSC():
    process_filial(
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" ")
    )

def nfePR():
    process_filial(
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" ")
    )


def nfeSP():
    process_filial(
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" "),
        os.getenv(" ")
    )

nfeWKI()
nfeSC()
nfePR()
nfeSP()

