import pygame
import time
from sys import exit

bkg = pygame.image.load("img/bkg.png")
pygame.init()
window = pygame.display.set_mode((1000, 600))  #window size


pygame.display.set_caption("SN-  PyGame") #name on upbar
clock = pygame.time.Clock()
#(from x, from y, lumghezza, larcghezza)
player = pygame.Rect(200, 300, 20, 25) #player quando punta sopra o sotto
player_l = pygame.Rect(200, 300, 25, 20) #player_l quando punta a estra o sinistra
s_l = False #verifica che il personaggio guarda a sinistra
s_u = False # verifica che il personaggio guarda sopra
ss_l = False #verifica che lultimo input era a o d
ss_u = False #verifica che lultimo input era w o s
s_done = False #verifica se il giocatore ha sprintato

pointlist = [
    (200, 0),
    (300, 0),
    (500, 600),
    (400, 600),


]
attack1 = pygame.draw.polygon(window, ("red"), pointlist, width=0)









while True:
    window.blit(bkg, (0, 0))
    if(ss_l == False):
        pygame.draw.rect(window, "red", player)
    else:
        pygame.draw.rect(window, "red", player_l)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #press the close button
            pygame.quit()
            exit()



#sprint:

    #sprint up
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            if s_done == False:
                if player.y >= 100:  
                    player.y -= 100
                    player_l.y -= 100
                    s_done = True
                else:  
                    player.y -= player.y
                    player_l.y -= player_l.y
                    s_done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            s_done = False

    #sprint left
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if s_done == False:
                    if player.x >= 100:  
                        player.x -= 100
                        player_l.x -= 100
                        s_done = True
                    else:  
                        player.x -= player.x
                        player_l.x -= player_l.x
                        s_done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            s_done = False

    #sprint right
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            if s_done == False:
                if player.x + 100 <= 1000:  
                    player.x += 100
                    player_l.x += 100
                    s_done = True
                else:  
                # Se lo supera, blocca entrambi gli oggetti esattamente a 1000
                    player.x = 1000 - 25
                    player_l.x = 1000 - 25
                    s_done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            s_done = False

    #sprint down
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                if s_done == False:
                    if player.y + 100 <= 600:  
                        player.y += 100
                        player_l.y += 100
                        s_done = True
                    else:  
                    # Se lo supera, blocca entrambi gli oggetti esattamente a 1000
                        player.y = 600 - 25
                        player_l.y = 600 - 25
                        s_done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            s_done = False

    if player.x > 1000:
        player.x = 1000
        player_l.x = 1000
#muovimenti
    kes = pygame.key.get_pressed()
    if kes[pygame.K_w] and (player and player_l).y - 10 >= 0 :
        player .y -= 10
        player_l .y -= 10
        ss_l = False
        ss_u = True
        s_u = True
        # il personaggio sta guardando sopra e l'ultimo input era w
    if kes[pygame.K_s] and (player and player_l).y + 10 + 25 <= 600:
        player .y += 10
        player_l .y += 10
        ss_l = False
        ss_u = True
        s_u = False
        # il personaggio sta guardando sotto e l'ultimo input era s
    if kes[pygame.K_a] and (player and player_l).x - 10 >= 0:
        player_l .x -= 10
        player .x -= 10
        ss_l = True
        ss_u = False
        s_l = True
        # il personaggio sta guardando a destra o a sinistra e l'ultimo input era a
    if kes[pygame.K_d] and (player and player_l).x + 10 + 25 <= 1000:
        player_l .x += 10
        player .x += 10
        ss_l = True
        ss_u = False
        s_l = False
        # il personaggio sta guardando a destra o a sinistra e l'ultimo input era d




    pygame.display.update()
    clock.tick(60)  #fps