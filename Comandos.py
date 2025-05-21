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
