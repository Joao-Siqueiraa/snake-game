import pygame
from pygame.locals import *
from sys import exit
import time
from random import randint

pygame.init()



largura = 640
altura = 480
xm = randint(40,640)
ym = randint(50,430)
frame = 20
xc = 100
yc = 420
v = 5
xcon = v
ycon = 0
pontos = 0
fonte = pygame.font.SysFont('arial',40,True,True) #fonte,tamanho,negrito,italico
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('jogo siqueirudo')
relogio = pygame.time.Clock()
lcobra = []
ci = 5
m = False

def ac(lcobra):
    for xey in lcobra:
        pygame.draw.rect(tela,(0,255,0),(xey[0],xey[1],20,20))

def rj():
    global pontos,ci,xc,yc,lcobra,lc,xm,ym,morreu
    pontos = 0
    ci = 5
    xc = 100
    yc = 420
    v = 5
    lcobra = []
    lc = []
    xm = randint(40,640)
    ym = randint(50,430)
    morreu = False


while True:
    relogio.tick(frame)
    tela.fill((0,0,0))
    mensagem = f'pontos:{pontos}'
    texto_formatado = fonte.render(mensagem,True,(255,255,255)) # mensagem, cerilhamento,cor
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if xcon == v:
                    pass
                else:
                    xcon = -v
                    ycon = 0
            if event.key == K_d:
                if xcon == -v:
                    pass
                else:
                    xcon = v
                    ycon = 0
            if event.key == K_w:
                if ycon == v:
                    pass
                else:
                    xcon = 0
                    ycon = -v
            if event.key == K_s:
                if ycon == -v:
                    pass
                else:
                    xcon = 0
                    ycon = v     
    xc = xc + xcon
    yc = yc + ycon       
    cobra = pygame.draw.rect(tela, (0,255,0),(xc,yc,20,20))
    maca = pygame.draw.rect(tela,(255,0,0), (xm,ym,20,20))

    if maca.colliderect(cobra):
      xm = randint(40,600)
      ym = randint(50,430)
      pontos = pontos + 1
      ci = ci + 1
      v = v + 0.5
    
    lc = []
    lc.append(xc)
    lc.append(yc)
    lcobra.append(lc)

    if lcobra.count(lc) > 1:
        fonte2 = pygame.font.SysFont('arial',20,True,True)
        mensagem1 = 'Game Over! Pressione R para jogar de novo'
        txtformatado = fonte2.render(mensagem1,True,(255,255,255))
        morreu = True
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        rj()
            tela.blit(txtformatado,(largura//2 - 200,altura//2))
            pygame.display.update()

    if xc > largura:
        xc = 0
    if xc < 0:
        xc = largura
    if yc < 0:
        yc = altura
    if yc > altura:
        yc = 0



    if len(lcobra) > ci:
        del lcobra[0]

    ac(lcobra)
    
      
    tela.blit(texto_formatado,(450,40)) #texto formatado, posiçao x e y
    pygame.display.update()

    pygame.font.get_fonts()