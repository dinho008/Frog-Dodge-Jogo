import os , time
import json
import speech_recognition as sr
import tkinter
import tkinter.messagebox as messagebox
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


def falar_nome():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Fale agora", "Por favor, fale o seu nickname...")
        try:
            audio = recognizer.listen(source, timeout=5)
            nome_falado = recognizer.recognize_google(audio, language='pt-BR')
            return nome_falado
        except sr.UnknownValueError:
            messagebox.showerror("Erro", "Não entendi o que você falou. Por favor, tente novamente ou digite seu nome.")
        except sr.RequestError:
            messagebox.showerror("Erro", "Não foi possível conectar ao serviço de reconhecimento.")
        except sr.WaitTimeoutError:
            messagebox.showerror("Erro", "Tempo de espera excedido. Por favor, tente novamente.")
    return None

