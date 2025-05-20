import pygame
import random
import math
import os 
import sys
import tkinter as tk
from Comandos import inicia_bando_dados
from Comandos import limparTela
from Comandos import aguarde
from Comandos import escreverDados
from tkinter import messagebox
import json

pygame.init()
inicia_bando_dados()

largura = 1000
altura = 700
fps = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura), 0)
pygame.display.set_caption('Fight in space')

branco = (255, 255, 255)
preto = (0, 0, 0)

fundo_incial = pygame.image.load("recursos/iniciogame.jpg")
fundo_jogo = pygame.image.load("recursos/Imagemjogo.png")
personagem_img = pygame.image.load("recursos/personagem.png")
projetil_img = pygame.image.load("recursos/projetil.png")
inimigo_img = pygame.image.load("recursos/Inimigo.png")
tela_de_morte = pygame.image.load("recursos/telaDeMorte.png")
personagem_img = pygame.transform.scale(personagem_img, (100, 100)) 
projetil_img = pygame.transform.scale(projetil_img, (80, 80))
inimigo_largura = 300
inimigo_altura = 300
inimigo_img = pygame.transform.scale(inimigo_img, (inimigo_largura, inimigo_altura))

fonteMenu = pygame.font.SysFont('comicsans', 24)
nome = ""

def iniciar_jogo():
    personagem_x = largura // 2 - 50
    personagem_y = altura - 150
    velocidade = 15

    projetil_x = random.randint(0, largura - 80)
    projetil_y = -80
    velocidade_projetil = 2
    aumento_velocidade = 0.01

    inimigo_x = largura // 2 - inimigo_largura // 2
    inimigo_y = 50

    rodando = True
    pausado = False 

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pausado = not pausado

        if pausado:
            texto_pausa = fonteMenu.render("GAME PAUSED - press space to continue", True, branco)
            texto_rect = texto_pausa.get_rect(center=(largura // 2, altura // 2))
            tela.blit(texto_pausa, texto_rect)
            pygame.display.update()
            fps.tick(10)
            continue

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            personagem_x -= velocidade
        if teclas[pygame.K_RIGHT]:
            personagem_x += velocidade

        if personagem_x < 0:
            personagem_x = 0
        elif personagem_x > largura - 100:
            personagem_x = largura - 100

        projetil_y += velocidade_projetil
        velocidade_projetil += aumento_velocidade

        if projetil_y > altura:
            projetil_x = random.randint(0, largura - 80)
            projetil_y = -80
            velocidade_projetil += 0.01

        personagem_rect = pygame.Rect(personagem_x, personagem_y, 100, 100)
        projetil_rect = pygame.Rect(projetil_x + 15, projetil_y + 15, 50, 50)

        if personagem_rect.colliderect(projetil_rect):
            game_over()

        tela.blit(fundo_jogo, (0, 0))
        tela.blit(inimigo_img, (inimigo_x, inimigo_y)) 
        tela.blit(personagem_img, (personagem_x, personagem_y)) 
        tela.blit(projetil_img, (projetil_x, projetil_y))

        dica_pause = fonteMenu.render("(press space to pause)", True, (180, 180, 180))
        tela.blit(dica_pause, (10, 10))

        pygame.display.update()
        fps.tick(60)

def game_over():
    tela.blit(tela_de_morte, (0, 0))
    fonte = pygame.font.SysFont('comicsans', 72)
    texto = fonte.render("GAME OVER", True, (255, 0, 0))
    rect = texto.get_rect(center=(largura // 2, altura // 2 + 100))
    tela.blit(texto, rect)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

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
            iniciar_jogo()

    def ao_fechar_janela():
        messagebox.showwarning("Aviso", "Você precisa digitar um nome para continuar!")

    root = tk.Tk()
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    root.title("Digite seu Nickname")
    root.protocol("WM_DELETE_WINDOW", ao_fechar_janela)

    entry_nome = tk.Entry(root)
    entry_nome.pack()

    botao = tk.Button(root, text="OK", command=obter_nome)
    botao.pack()

    root.mainloop()

def start():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    while True:
        mouse_pos = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(mouse_pos):
                    jogar()
                if quitButton.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        tela.blit(fundo_incial, (0, 0))

        sombra_start = fonteMenu.render("Iniciar Game", True, (50, 50, 50))
        startTexto = fonteMenu.render("Iniciar Game", True, branco)
        start_rect = startTexto.get_rect(topleft=(25, 12))
        tela.blit(sombra_start, (start_rect.x + 2, start_rect.y + 2))
        tela.blit(startTexto, start_rect)

        sombra_quit = fonteMenu.render("Sair do Game", True, (50, 50, 50))
        quitTexto = fonteMenu.render("Sair do Game", True, branco)
        quit_rect = quitTexto.get_rect(topleft=(25, 62))
        tela.blit(sombra_quit, (quit_rect.x + 2, quit_rect.y + 2))
        tela.blit(quitTexto, quit_rect)

        startButton = start_rect
        quitButton = quit_rect

        if startButton.collidepoint(mouse_pos) or quitButton.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()
        fps.tick(60)

start()