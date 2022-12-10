import pygame, sys
from pygame import mixer
from scripts.frog import Frog
from scripts.spritesheet import Spritesheet
from scripts.car import Car
from scripts.log import Log
from scripts.goal import Goal
from scripts.font import Font

#configurações iniciais
#janela
largura_tela = 672
altura_tela = 768
#tela do jogo
largura_render = 224
altura_render = 256

pygame.init()
mixer.init()

#set display
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Frogger")
cor_agua = (0,0,71)
render = pygame.Surface((largura_render,altura_render))

#set clock
clock = pygame.time.Clock()

#carregar graficos
graphics = Spritesheet("frogger_graphics.png")
fonte = Font(graphics)
grama_roxa = graphics.get_sprite(135,196,16,16)
chegada_entrada = graphics.get_sprite(1,188,32,24)
chegada_grama = graphics.get_sprite(35,188,8,24)
chegada = [chegada_entrada, chegada_grama]
sapo_parado = graphics.get_sprite(1,1,16,16)
sapo_pulando = graphics.get_sprite(19,1,16,16)
sapo_vida = graphics.get_sprite(37,214,8,8)
carro_1 = graphics.get_sprite(1,116,16,16)
carro_2 = graphics.get_sprite(19,116,16,16)
carro_3 = graphics.get_sprite(37,116,16,16)
carro_4 = graphics.get_sprite(55,116,16,16)
carro_5 = graphics.get_sprite(73,116,32,16)
tronco_inicio = graphics.get_sprite(1,134,16,16)
tronco_meio = graphics.get_sprite(19,134,16,16)
tronco_fim = graphics.get_sprite(37,134,16,16)
tronco_g = [tronco_inicio, tronco_meio, tronco_fim]
tartaruga_f1 = graphics.get_sprite(1,152,16,16)
tartaruga_f2 = graphics.get_sprite(19,152,16,16)
tartaruga_f3 = graphics.get_sprite(37,152,16,16)
tartaruga_f4 = graphics.get_sprite(55,152,16,16)
tartaruga_f5 = graphics.get_sprite(73,152,16,16)
tartaruga_g = [tartaruga_f1, tartaruga_f2, tartaruga_f3, tartaruga_f4, tartaruga_f5]
sapo_chegada = graphics.get_sprite(45,196,16,16)

#carreegar sons
s_vitoria = mixer.Sound("./sounds/vitoria.wav")
s_gameover = mixer.Sound("./sounds/gameover.wav")
s_opengame = mixer.Sound("./sounds/openstarter.wav")

#menu state
def title_screen():
    counter = 0
    blink = 1
    blinked = True
    F = graphics.get_sprite(1,232,16,16)
    R = graphics.get_sprite(19,232,16,16)
    O = graphics.get_sprite(37,232,16,16)
    G = graphics.get_sprite(55,232,16,16)
    E = graphics.get_sprite(73,232,16,16)
    while True:
        #set frame_rate + deltatime
        dt = clock.tick(30)/1000

        #loop de eventos
        for event in pygame.event.get():
            #fechar a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    s_opengame.play()
                    game()

        render.fill('black')
        render.blit(F, (32, 92))
        render.blit(R, (56, 92))
        render.blit(O, (80, 92))
        render.blit(G, (104, 92))
        render.blit(G, (128, 92))
        render.blit(E, (152, 92))
        render.blit(R, (176, 92))

        #texto piscante
        counter += 1*dt
        if counter >= 1:
            counter = 0
            if blinked == True:
                blinked = False
            else:
                blinked = True

        if blinked:
            fonte.write(render, ((largura_render/2)-(8*7)-4), (8*20), "pressione enter")

        fonte.write(render, (4+(largura_render/2)-(8*8)), altura_render-24, "college project")
        fonte.write(render, ((largura_render/2)-(8*2)), altura_render-16, "2022")
        #redimensiona o jogo para o tamanho da janela
        render_sized = pygame.transform.scale(render, (largura_tela, altura_tela))

        #renderiza o jogo na janela
        screen.blit(render_sized, (0,0))

        pygame.display.update()

#game state
def game():
    #set objects
    sapo = Frog(largura_render/2, altura_render-(16*2), (sapo_parado,sapo_pulando))
    carro_rosa_1 = Car(largura_render-(16*9),altura_render-(16*5),-1,36,carro_1)
    carro_rosa_2 = Car(largura_render-(16*5),altura_render-(16*5),-1,36,carro_1)
    carro_rosa_3 = Car(largura_render,altura_render-(16*5),-1,36,carro_1)
    caminhao_1 = Car(largura_render-16, altura_render-(16*7), -1, 42, carro_5)
    caminhao_2 = Car(largura_render-(16*8), altura_render-(16*7), -1, 42, carro_5)
    carro_amarelo_1 = Car(largura_render, altura_render-(16*3), -1, 32, carro_2)
    carro_amarelo_2 = Car(largura_render-(16*5), altura_render-(16*3), -1, 32, carro_2)
    carro_amarelo_3 = Car(largura_render-(16*9), altura_render-(16*3), -1, 32, carro_2)
    carro_verde_1 = Car(largura_render, altura_render-(16*4), 1, 38, carro_4)
    carro_verde_2 = Car(largura_render-(16*5), altura_render-(16*4), 1, 38, carro_4)
    carro_verde_3 = Car(largura_render-(16*9), altura_render-(16*4), 1, 38, carro_4)
    carro_corrida = Car(largura_render, altura_render-(16*6), 1, 100, carro_3)
    tora_1 = Log((16*2), altura_render-(16*10), 3, 1, 20, tronco_g, "log")
    tora_2 = Log((16*7), altura_render-(16*10), 3, 1, 20, tronco_g, "log")
    tora_3 = Log((16*12), altura_render-(16*10), 3, 1, 20, tronco_g, "log")
    tora_4 = Log(0, altura_render-(16*13), 4, 1, 25, tronco_g, "log")
    tora_5 = Log((16*6), altura_render-(16*13), 4, 1, 25, tronco_g, "log")
    tora_6 = Log((16*11), altura_render-(16*13), 4, 1, 25, tronco_g, "log")
    tora_7 = Log(0, altura_render-(16*11), 6, 1, 36, tronco_g, "log")
    tora_8 = Log((16*8), altura_render-(16*11), 6, 1, 36, tronco_g, "log")
    tartaruga_l1_1 = Log(0, altura_render-(16*9), 3, -1, 32, tartaruga_g, "turtle")
    tartaruga_l1_2 = Log((16*4), altura_render-(16*9), 3, -1, 32, tartaruga_g, "turtle")
    tartaruga_l1_3 = Log((16*8), altura_render-(16*9), 3, -1, 32, tartaruga_g, "turtle")
    tartaruga_l1_4 = Log((16*12), altura_render-(16*9), 3, -1, 32, tartaruga_g, "turtle", True)
    tartaruga_l2_1 = Log((16*1), altura_render-(16*12), 2, -1, 32, tartaruga_g, "turtle")
    tartaruga_l2_2 = Log((16*5), altura_render-(16*12), 2, -1, 32, tartaruga_g, "turtle")
    tartaruga_l2_3 = Log((16*9), altura_render-(16*12), 2, -1, 32, tartaruga_g, "turtle")
    tartaruga_l2_4 = Log((16*13), altura_render-(16*12), 2, -1, 32, tartaruga_g, "turtle", True)
    chegadas = [Goal(8+(16*n), 32, sapo_chegada) for n in range(0,14,3)]
    print(chegadas)

    veiculos = [
        carro_rosa_1,carro_rosa_2,carro_rosa_3,caminhao_1,caminhao_2,
        carro_amarelo_1, carro_amarelo_2, carro_amarelo_3, carro_corrida,
        carro_verde_1, carro_verde_2, carro_verde_3
        ]

    madeiras = [
        tora_1, tora_2, tora_3, tora_4, tora_5, tora_6, tora_7, tora_8, tartaruga_l1_1, tartaruga_l1_2, tartaruga_l1_3, tartaruga_l1_4,
        tartaruga_l2_1, tartaruga_l2_2, tartaruga_l2_3, tartaruga_l2_4
    ]

    colisao_perigosa = [x.rect for x in veiculos]

    pontos = 0

    #set hi-score
    try:
        hi_score_file = open("highscore.txt", "r")
    except:
        hi_score_file = open("highscore.txt", "w+")
        hi_score_file.write("0")

    hi = int(hi_score_file.read())

    hi_score_file.close()

    while True:

        #deltatime
        dt = clock.tick(60)/1000

        if all(goal.catch for goal in chegadas):
            s_vitoria.play()
            for goal in chegadas:
                goal.catch = False

        #loop de eventos
        for event in pygame.event.get():

            #fechar a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #entrada de teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    sapo.move('left')
                if event.key == pygame.K_RIGHT  or event.key == pygame.K_d:
                    sapo.move('right')
                if event.key == pygame.K_UP  or event.key == pygame.K_w:
                    sapo.move('up')
                if event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                    sapo.move('down')

        if sapo.vidas == 0:
            if pontos > hi:
                hi_score_file = open("highscore.txt", "w")
                hi_score_file.write(str(pontos))
                hi_score_file.close()
            gameover_screen()
            break
        
        sapo.update(dt)
        pontos += sum([goal.update(sapo) for goal in chegadas])
        sapo.attach(madeiras, dt)
        sapo.kill(colisao_perigosa)

        #desenha o frame
        render.fill('black')
        render.fill(cor_agua, (0,0, largura_render, altura_render//2))

        fonte.write(render, 32, 0, "1-up")
        fonte.write(render, 80, 0, "hi-score")
        fonte.write(render, 24, 8, f"{pontos:05}")
        fonte.write(render, 88, 8, f"{hi:05}")

        for up in range(sapo.vidas):
            render.blit(sapo_vida, ((8*up), altura_render-16))

        for h in (128,224):
            for w in range(0, largura_render, 16):
                render.blit(grama_roxa, (w,h))

        col = 0
        idx = 0
        while col < largura_render:
            if idx > 1:
                idx = 0

            if idx == 1:
                for n in range(2): 
                    render.blit(chegada[idx], (col, 24))
                    col += chegada[idx].get_width()
            else:
                render.blit(chegada[idx], (col, 24))
                col += chegada[idx].get_width()

            idx += 1

        for madeira in madeiras:
            madeira.draw_log(render, dt)

        [goal.draw(render) for goal in chegadas]

        sapo.draw(render)
        for carro in veiculos:
            carro.draw(render, dt)

        #redimensiona o jogo para o tamanho da janela
        render_sized = pygame.transform.scale(render, (largura_tela, altura_tela))

        #renderiza o jogo na janela
        screen.blit(render_sized, (0,0))

        pygame.display.update()

#gameover state
def gameover_screen():
    time = 5
    counter = 0
    s_gameover.play(2)
    while True:

        #deltatime
        dt = clock.tick(1)/1000

        #eventos
        for event in pygame.event.get():

            #fechar a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        render.fill('black')

        counter += 1*dt
        fonte.write(render, (largura_render/2-4)-32, altura_render/2-4, "game over")
        if counter >= 5:
            break

        #redimensiona o jogo para o tamanho da janela
        render_sized = pygame.transform.scale(render, (largura_tela, altura_tela))

        #renderiza o jogo na janela
        screen.blit(render_sized, (0,0))
        pygame.display.update()

title_screen()