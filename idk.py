import pygame
import time
import random  
from sys import exit

pygame.init()
window = pygame.display.set_mode((1000, 600))  # window size
bkg = pygame.image.load("img/bkg.png")

pygame.display.set_caption("SN-  PyGame")  # name on upbar
clock = pygame.time.Clock()

pygame.mixer.music.load("music/Creo_Crazy.mp3")

player = pygame.Rect(200, 300, 20, 25)  # player quando punta sopra o sotto
player_l = pygame.Rect(200, 300, 25, 20) # player quando punta a destra o sinistra

# attacchi
atck_1 = pygame.Rect (0, 300, 1000, 100)
atck_2 = pygame.Rect (0, 100, 1000, 100)
atck_3 = pygame.Rect (0, 400, 1000, 100)

s_l = False  
s_u = False  
ss_l = False  
ss_u = False  
s_done = False  

# --- CONFIGURAZIONE TIMER E ATTACCHI ---
EVENTO_CANCELLA_ATTACCO_1 = pygame.USEREVENT + 1
EVENTO_CANCELLA_ATTACCO_2 = pygame.USEREVENT + 2
evento_del_atc_3 = pygame.USEREVENT + 3
evento_del_atc_3_l = pygame.USEREVENT + 4
evento_del_atc_3_t = pygame.USEREVENT + 5
evento_del_atc_3_t_h = pygame.USEREVENT + 6

# Variabili di stato per decidere se mostrare gli attacchi sullo schermo
mostra_attacco1 = False
mostra_attacco2 = False
sh_atc3 = False
sh_atc3_h = False
sh_atc3_t = False
sh_atc3_t_h = False

# life
vite = 3
game_over = False
tempo_ultimo_danno = 0  
invulnerabilita_durata = 1000  

durata_shake = 0       
intensita_shake = 6   

font = pygame.font.SysFont(None, 30)
font_grande = pygame.font.SysFont(None, 50)

while True:
    # shake
    shake_x = 0
    shake_y = 0
    if durata_shake > 0:
        shake_x = random.randint(-intensita_shake, intensita_shake)
        shake_y = random.randint(-intensita_shake, intensita_shake)
        durata_shake -= 1  

    # -bkg
    window.blit(bkg, (0 + shake_x, 0 + shake_y))
    
    # da player
    if not game_over:
        tempo_attuale = pygame.time.get_ticks()
        if tempo_attuale - tempo_ultimo_danno > invulnerabilita_durata or (tempo_attuale // 100) % 2 == 0:
            if not ss_l:
                rect_disegno = player.move(shake_x, shake_y)
                pygame.draw.rect(window, "red", rect_disegno)
            else:
                rect_disegno_l = player_l.move(shake_x, shake_y)
                pygame.draw.rect(window, "red", rect_disegno_l)

    # atck
    if mostra_attacco1:
        atck_1_disegno = atck_1.move(shake_x, shake_y)
        pygame.draw.rect(window, (71, 27, 24), atck_1_disegno)
        
    if mostra_attacco2:
        atck_2_disegno = atck_1.move(shake_x, shake_y)
        pygame.draw.rect(window, "red", atck_2_disegno)

    if sh_atc3:
        atck_3_disegno = atck_2.move(shake_x, shake_y)
        pygame.draw.rect(window, (71, 27, 24), atck_3_disegno)

    if sh_atc3_h:
        atck_3_h_disegno = atck_2.move(shake_x, shake_y)  
        pygame.draw.rect(window, "red", atck_3_h_disegno) 

    if sh_atc3_t:
        atck_3_t_disegno = atck_3.move(shake_x, shake_y)
        pygame.draw.rect(window, (71, 27, 24), atck_3_t_disegno) 

    if sh_atc3_t_h:  
        atck_3_t_h_disegno = atck_3.move(shake_x, shake_y)
        pygame.draw.rect(window, "red", atck_3_t_h_disegno) 

    # gui
    testo_vite = font.render(f"Vite: {vite}", True, "white")
    window.blit(testo_vite, (20, 20))

    if game_over:
        testo_game_over = font_grande.render("GAME OVER", True, "red")
        testo_restart = font.render("Premi SPAZIO per ricominciare", True, "white")
        window.blit(testo_game_over, (380, 230))
        window.blit(testo_restart, (330, 300))

    # damage
    if not game_over:
        player_corrente = player_l if ss_l else player
        subisce_danno = False
        tempo_attuale = pygame.time.get_ticks()

        if tempo_attuale - tempo_ultimo_danno > invulnerabilita_durata:
            if mostra_attacco2 and player_corrente.colliderect(atck_1):
                subisce_danno = True
            elif sh_atc3_h and player_corrente.colliderect(atck_2):
                subisce_danno = True
            elif sh_atc3_t_h and player_corrente.colliderect(atck_3):
                subisce_danno = True

        if subisce_danno:
            vite -= 1
            tempo_ultimo_danno = tempo_attuale  
            
            if vite <= 0:
                game_over = True
                pygame.mixer.music.stop() 
            else:
                forza_knockback = 50
                if ss_l:
                    if s_l: player.x += forza_knockback; player_l.x += forza_knockback
                    else: player.x -= forza_knockback; player_l.x -= forza_knockback
                else:
                    if s_u: player.y += forza_knockback; player_l.y += forza_knockback
                    else: player.y -= forza_knockback; player_l.y -= forza_knockback

                if player.x < 0: player.x, player_l.x = 0, 0
                if player.x > 1000 - 25: player.x, player_l.x = 1000 - 25, 1000 - 25
                if player.y < 0: player.y, player_l.y = 0, 0
                if player.y > 600 - 25: player.y, player_l.y = 600 - 25, 600 - 25

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    vite = 3
                    game_over = False
                    player.x, player.y = 200, 300
                    player_l.x, player_l.y = 200, 300
                    mostra_attacco1 = mostra_attacco2 = False
                    sh_atc3 = sh_atc3_h = sh_atc3_t = sh_atc3_t_h = False
                    durata_shake = 0
                else:
                    if not mostra_attacco1 and not mostra_attacco2 and not sh_atc3 and not sh_atc3_h and not sh_atc3_t and not sh_atc3_t_h:
                        mostra_attacco1 = True  
                        pygame.time.set_timer(EVENTO_CANCELLA_ATTACCO_1, 500, loops=1)
                        pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
            
            if event.key in [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN]:
                s_done = False


        if event.type == pygame.KEYUP and not game_over:
            if event.key == pygame.K_UP and not s_done:
                if player.y >= 100: player.y -= 100; player_l.y -= 100; s_done = True
                else: player.y = 0; player_l.y = 0; s_done = True
            elif event.key == pygame.K_LEFT and not s_done:
                if player.x >= 100: player.x -= 100; player_l.x -= 100; s_done = True
                else: player.x = 0; player_l.x = 0; s_done = True
            elif event.key == pygame.K_RIGHT and not s_done:
                if player.x + 100 <= 1000: player.x += 100; player_l.x += 100; s_done = True
                else: player.x = 1000 - 25; player_l.x = 1000 - 25; s_done = True
            elif event.key == pygame.K_DOWN and not s_done:
                if player.y + 100 <= 600: player.y += 100; player_l.y += 100; s_done = True
                else: player.y = 600 - 25; player_l.y = 600 - 25; s_done = True

        #the level itself
        if not game_over:
            if event.type == EVENTO_CANCELLA_ATTACCO_1:
                mostra_attacco1 = False  
                mostra_attacco2 = True   
                pygame.time.set_timer(EVENTO_CANCELLA_ATTACCO_2, 500, loops=1)
                durata_shake = 6 

            elif event.type == EVENTO_CANCELLA_ATTACCO_2:
                mostra_attacco2 = False
                sh_atc3 = True
                pygame.time.set_timer(evento_del_atc_3, 500, loops=1)

            elif event.type == evento_del_atc_3:
                sh_atc3 = False
                sh_atc3_h = True
                pygame.time.set_timer(evento_del_atc_3_l, 500, loops=1)
                durata_shake = 6 

            elif event.type == evento_del_atc_3_l:
                sh_atc3_h = False
                sh_atc3_t = True
                pygame.time.set_timer(evento_del_atc_3_t, 500, loops=1)

            elif event.type == evento_del_atc_3_t:
                sh_atc3_t = False
                sh_atc3_t_h = True
                pygame.time.set_timer(evento_del_atc_3_t_h, 500, loops=1)
                durata_shake = 6  

            elif event.type == evento_del_atc_3_t_h:
                sh_atc3_t_h = False
                mostra_attacco1 = True


    # movimenti
    if not game_over:
        kes = pygame.key.get_pressed()
        if kes[pygame.K_w] and (player.y - 10 >= 0):
            player.y -= 10; player_l.y -= 10; ss_l = False; ss_u = True; s_u = True
        if kes[pygame.K_s] and (player.y + 10 + 25 <= 600):
            player.y += 10; player_l.y += 10; ss_l = False; ss_u = True; s_u = False
        if kes[pygame.K_a] and (player.x - 10 >= 0):
            player_l.x -= 10; player.x -= 10; ss_l = True; ss_u = False; s_l = True
        if kes[pygame.K_d] and (player.x + 10 + 25 <= 1000):
            player_l.x += 10; player.x += 10; ss_l = True; ss_u = False; s_l = False

    pygame.display.update()
    clock.tick(60)  # fps

