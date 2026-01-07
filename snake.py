import pygame
from pygame.locals import *
import random

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
POS_INICIAL_Y = WINDOWS_HEIGHT/2 #PARA FICAR NO MEIO DA TELA
POS_INICIAL_X = WINDOWS_WIDTH/2 #PARA FICAR NO MEIO DA TELA
BLOCK = 10

pygame.font.init()
fonte = pygame.font.SysFont('Franklin Gothic Medium', 35, True, True)

pontos = 0
velocidade = 12

def game_over():
    pygame.quit()
    quit()

pygame.display.set_caption('Snake Game')

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
cobra_surface.fill((0,0,205))
direcao = K_LEFT

maca_surface = pygame.Surface((BLOCK, BLOCK))
maca_surface.fill((255,0,0))
maca_pos = gera_pos()

pedra_pos = []
pedra_surface = pygame.Surface((BLOCK, BLOCK))
pedra_surface.fill((0,0,0))

while True:
    pygame.time.Clock().tick(velocidade)
    window.fill((0, 255, 0))

    mensagem = f'Pontos: {pontos }'
    texto = fonte.render(mensagem, True, (255,255,255))

    for evento in pygame.event.get():

        if evento.type == QUIT:
            pygame.quit()
            quit()

        elif evento.type == KEYDOWN:
            if evento.key in  [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                if evento.key == K_UP and direcao == K_DOWN:
                    continue
                elif evento.key == K_DOWN and direcao == K_UP:
                    continue
                elif evento.key == K_LEFT and direcao == K_RIGHT:
                    continue
                elif evento.key == K_RIGHT and direcao == K_LEFT:
                    continue
                
                direcao = evento.key

    window.blit(maca_surface, maca_pos)

    if (colisao(cobra_pos[0], maca_pos)):
        cobra_pos.append((-10, -10))
        maca_pos = gera_pos()
        pedra_pos.append(gera_pos())
        pontos += 1
        if pontos % 3 ==0:
            velocidade += 2

    for pos in pedra_pos:
        if colisao(cobra_pos[0], pos):
            game_over()
        window.blit(pedra_surface, pos)

    for pos in cobra_pos:
        window.blit(cobra_surface, pos)

    for i in range(len(cobra_pos)-1,0, -1):
        if colisao(cobra_pos[0], cobra_pos[i]):
            game_over()
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

    window.blit(texto,(420, 30))
    pygame.display.update()