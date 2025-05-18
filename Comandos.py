import os , time
import json
from datetime import datetime

def limparTela():
    os.system('cls')
    
def aguarde(segundos):
    time.sleep(segundos)

def inicia_bando_dados():
    try:
        banco = open('log.dat', 'r')
    except:
        print('O banco de dados não existe, criando...')
        banco = open('log.dat', 'w')

def escreverDados(nome, pontos):
    
    banco = open("base.atitus","r")
    dados = banco.read()
    banco.close()
    print("dados",type(dados))
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}
        
    data_br = datetime.now().strftime("%d/%m/%Y")
    dadosDict[nome] = (pontos, data_br)
    
    banco = open("base.atitus","w")
    banco.write(json.dumps(dadosDict))
    banco.close()