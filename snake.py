import pygame
from pygame.locals import *
import random

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
POS_INICIAL_Y = WINDOWS_HEIGHT/2 #PARA FICAR NO MEIO DA TELA
POS_INICIAL_X = WINDOWS_WIDTH/2 #PARA FICAR NO MEIO DA TELA
BLOCK = 10

def game_over():
    pygame.quit()
    quit()

#confere se a cobra ta na janela
def verifica_margens(pos):
    if 0 <= pos[0] < WINDOWS_WIDTH and  0 <= pos[1] < WINDOWS_HEIGHT:
        return False
    else:
        return True
    
def gera_pos():
    x = random.randint(0, WINDOWS_WIDTH)
    y = random.randint(0, WINDOWS_HEIGHT)
    return x // BLOCK * BLOCK , y // BLOCK * BLOCK

def colisao(pos1, pos2):
    return pos1 == pos2


pygame.init()
window = pygame.display.set_mode((WINDOWS_HEIGHT, WINDOWS_WIDTH))

cobra_pos = [(POS_INICIAL_X,POS_INICIAL_Y), (POS_INICIAL_X + BLOCK, POS_INICIAL_Y), (POS_INICIAL_X + 2 * BLOCK, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK, BLOCK))
direcao = K_RIGHT

maca_surface = pygame.Surface((BLOCK, BLOCK))
maca_surface.fill((255,0,0))
maca_pos = gera_pos()


while True:
    pygame.time.Clock().tick(12)
    window.fill((0, 255, 0))

    for evento in pygame.event.get():

        if evento.type == QUIT:
            pygame.quit()
            quit()

        elif evento.type == KEYDOWN:
            if evento.key in  [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao = evento.key

    window.blit(maca_surface, maca_pos)

    if (colisao(cobra_pos[0], maca_pos)):
        cobra_pos.append((-10, -10))
        maca_pos = gera_pos()

    for pos in cobra_pos:
        window.blit(cobra_surface, pos)

    for i in range(len(cobra_pos)-1,0, -1):
        cobra_pos[i] = cobra_pos[i - 1]

    if verifica_margens(cobra_pos[0]):
        game_over()

#movimentação lateral e horizontal
    if direcao == K_RIGHT:
        cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1] #movimentação para a direita
    elif direcao == K_LEFT:
        cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1] #movimentação para a esquerda
    elif direcao == K_UP:
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK # movimentação para cima
    elif direcao == K_DOWN:
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK # movimentação para baixo


    pygame.display.update()