import pygame
import time
import random

# Inicialização
pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Configurações da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha com Pausa')

# Configurações do jogo
clock = pygame.time.Clock()
tamanho_bloco = 10
velocidade_cobra = 15

# Fontes
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)
fonte_mensagem = pygame.font.SysFont("bahnschrift", 25)

def mostra_pontuacao(pontuacao):
    texto = fonte_pontuacao.render(f"Pontos: {pontuacao}", True, preto)
    tela.blit(texto, [10, 10])

def desenha_cobra(tamanho_bloco, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

def mensagem(txt, cor):
    texto = fonte_mensagem.render(txt, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def jogo():
    game_over = False
    game_close = False
    pausado = False  # Variável para controlar o estado de pausa
    
    # Posição inicial da cobra
    x1 = largura / 2
    y1 = altura / 2
    
    # Movimento inicial
    x1_mudanca = 0
    y1_mudanca = 0
    
    # Corpo da cobra
    lista_cobra = []
    comprimento_cobra = 1
    
    # Posição da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
    
    while not game_over:
        while game_close:
            tela.fill(branco)
            mensagem("Fim de jogo! Pressione Q-Sair ou C-Jogar novamente", vermelho)
            mostra_pontuacao(comprimento_cobra - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                # Pausa/despausa o jogo com a tecla P
                if event.key == pygame.K_p:
                    pausado = not pausado
                
                # Movimento (só funciona se o jogo não estiver pausado)
                if not pausado:
                    if event.key == pygame.K_LEFT and x1_mudanca == 0:
                        x1_mudanca = -tamanho_bloco
                        y1_mudanca = 0
                    elif event.key == pygame.K_RIGHT and x1_mudanca == 0:
                        x1_mudanca = tamanho_bloco
                        y1_mudanca = 0
                    elif event.key == pygame.K_UP and y1_mudanca == 0:
                        y1_mudanca = -tamanho_bloco
                        x1_mudanca = 0
                    elif event.key == pygame.K_DOWN and y1_mudanca == 0:
                        y1_mudanca = tamanho_bloco
                        x1_mudanca = 0
        
        # Se o jogo estiver pausado, não atualiza a posição da cobra
        if pausado:
            mensagem("PAUSADO - Pressione P para continuar", azul)
            pygame.display.update()
            continue  # Pula o resto do loop enquanto pausado
        
        # Verifica se bateu na parede
        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_close = True
        
        # Atualiza a posição da cobra
        x1 += x1_mudanca
        y1 += y1_mudanca
        
        # Desenha a tela
        tela.fill(branco)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        
        # Atualiza o corpo da cobra
        cabeca_cobra = [x1, y1]
        lista_cobra.append(cabeca_cobra)
        
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]
        
        # Verifica se bateu no próprio corpo
        for bloco in lista_cobra[:-1]:
            if bloco == cabeca_cobra:
                game_close = True
        
        desenha_cobra(tamanho_bloco, lista_cobra)
        mostra_pontuacao(comprimento_cobra - 1)
        pygame.display.update()
        
        # Verifica se comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1
        
        clock.tick(velocidade_cobra)
    
    pygame.quit()
    quit()

# Inicia o jogo
jogo()