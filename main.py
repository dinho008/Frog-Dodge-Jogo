import pygame
import random
import math
import os 
import tkinter as tk
from Comandos import inicia_bando_dados
from Comandos import limparTela
from Comandos import aguarde
from Comandos import escreverDados
from logging import root
from tkinter import messagebox
import json

pygame.init()
inicia_bando_dados()
largura = 1000
altura = 700
fps = pygame.time.Clock()
dimensao = (largura, altura)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Frog Dodge Game')
branco = (255,255,255)
preto = (0,0,0)
fundoincial = pygame.image.load("recursos/iniciogame.jpg")
fundojogo = pygame.image.load("recursos/imagemjogo.png")
fonteMenu = pygame.font.SysFont('comicsans', 18)

def jogar():
    largura_janela = 300
    altura_janela = 50

    def obter_nome():
        global nome
        nome = entry_nome.get() 
        if not nome.strip():  
            messagebox.showwarning("Aviso", "Por favor, digite seu nome!")  
        else:
            root.destroy()

    def ao_fechar_janela():
        messagebox.showwarning("Aviso", "Você precisa digitar um nome para continuar!")

    root = tk.Tk()
    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()
    x = (largura - largura_janela) // 2
    y = (altura - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    root.title("Digite seu Nickname")
    root.protocol("WM_DELETE_WINDOW", ao_fechar_janela)  # nova função aqui

    entry_nome = tk.Entry(root)
    entry_nome.pack()

    botao = tk.Button(root, text="OK", command=obter_nome)
    botao.pack()

    root.mainloop()

def start():
    larguraButtonStart = 150
    alturaButtonStart  = 40
    larguraButtonQuit = 150
    alturaButtonQuit  = 40
    

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit  = 35

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                # Verifica se o clique foi dentro do retângulo
                if startButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()
                if quitButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonQuit = 150
                    alturaButtonQuit  = 40
                    quit()

        tela.blit(fundoincial, (0,0))

        startButton = pygame.draw.rect(tela, branco, (10,10, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25,12))
        
        quitButton = pygame.draw.rect(tela, branco, (10,60, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (25,62))

        pygame.display.update()
        fps.tick(60)

start()