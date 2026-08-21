import pygame
import time
import random  
from sys import exit

pygame.init()
window = pygame.display.set_mode((1000, 600))  # window size
bkg = pygame.image.load("img/bkg.png")

pygame.display.set_caption("SN-  PyGame")  # name on upbar
clock = pygame.time.Clock()

# --- MODIFICA 1: Rimosso il load da qui per evitare il blocco all'avvio ---

player = pygame.Rect(200, 300, 20, 25)  # player quando punta sopra o sotto
player_l = pygame.Rect(200, 300, 25, 20) #player quando punta a destra o sinistra

#attacchi
atck_1 = pygame.Rect (0, 0, 1000, 100)
atck_2 = pygame.Rect (0, 100, 1000, 100)
atck_3 = pygame.Rect (0, 200, 1000, 100)
atck_4 = pygame.Rect (0, 300, 1000, 100)
atck_5 = pygame.Rect (0, 400, 1000, 100)
atck_6 = pygame.Rect (0, 500, 1000, 100)
atck_1_v = pygame.Rect (0, 0, 100, 600)
atck_2_v = pygame.Rect (100, 0, 100, 600)
atck_3_v = pygame.Rect (200, 0, 100, 600)
atck_4_v = pygame.Rect (300, 0, 100, 600)
atck_5_v = pygame.Rect (400, 0, 100, 600)
atck_6_v = pygame.Rect (500, 0, 100, 600)
atck_7_v = pygame.Rect (600, 0, 100, 600)
atck_8_v = pygame.Rect (700, 0, 100, 600)
atck_9_v = pygame.Rect (800, 0, 100, 600)
atck_10_v = pygame.Rect (900, 0, 100, 600)

s_l = False  
s_u = False  
ss_l = False  
ss_u = False  
s_done = False  

EVENTO_CANCELLA_ATTACCO_1 = pygame.USEREVENT + 1
EVENTO_CANCELLA_ATTACCO_2 = pygame.USEREVENT + 2
evento_del_atc_3 = pygame.USEREVENT + 3
evento_del_atc_3_l = pygame.USEREVENT + 4
evento_del_atc_3_t = pygame.USEREVENT + 5
evento_del_atc_3_t_h = pygame.USEREVENT + 6
s_atc = pygame.USEREVENT + 7
s_atc_h = pygame.USEREVENT + 8
s_atc_h_del = pygame.USEREVENT + 9
s_1 = pygame.USEREVENT + 10
s_2 = pygame.USEREVENT + 11
s_3 = pygame.USEREVENT + 12
s_4 = pygame.USEREVENT + 13
s_5 = pygame.USEREVENT + 14
s_6 = pygame.USEREVENT + 15
s_7 = pygame.USEREVENT + 16
s_8 = pygame.USEREVENT + 17
s_9 = pygame.USEREVENT + 18
s_10 = pygame.USEREVENT + 19
charge = pygame.USEREVENT + 20
s_11 = pygame.USEREVENT + 21
s_12 = pygame.USEREVENT + 22
s_13 = pygame.USEREVENT + 23
s_14 = pygame.USEREVENT + 24
s_15 = pygame.USEREVENT + 25
s_16 = pygame.USEREVENT + 26
s_17 = pygame.USEREVENT + 27
s_18 = pygame.USEREVENT + 28
s_19 = pygame.USEREVENT + 29
s_20 = pygame.USEREVENT + 30
s_21 = pygame.USEREVENT + 31
s_22 = pygame.USEREVENT + 32
s_23 = pygame.USEREVENT + 33
s_24 = pygame.USEREVENT + 34
s_25 = pygame.USEREVENT + 35
s_26 = pygame.USEREVENT + 36
s_27 = pygame.USEREVENT + 37
s_28 = pygame.USEREVENT + 38
s_29 = pygame.USEREVENT + 39
s_30 = pygame.USEREVENT + 40
# Variabili di stato per decidere se mostrare gli attacchi sullo schermo
mostra_attacco1 = False
mostra_attacco2 = False
sh_atc3 = False
sh_atc3_h = False
sh_atc3_t = False
sh_atc3_t_h = False

sh_atc_1 = False
sh_atc_2 = False
sh_atc_3 = False
sh_atc_4 = False
sh_atc_5 = False
sh_atc_6 = False
sh_atc_v_1 = False
sh_atc_v_2 = False
sh_atc_v_3 = False
sh_atc_v_4 = False
sh_atc_v_5 = False
sh_atc_v_6 = False
sh_atc_v_7 = False
sh_atc_v_8 = False
sh_atc_v_9 = False
sh_atc_v_10 = False

sh_atc_h_1 = False
sh_atc_h_2 = False
sh_atc_h_3 = False
sh_atc_h_4 = False
sh_atc_h_5 = False
sh_atc_h_6 = False
sh_atc_h_v_1 = False
sh_atc_h_v_2 = False
sh_atc_h_v_3 = False
sh_atc_h_v_4 = False
sh_atc_h_v_5 = False
sh_atc_h_v_6 = False
sh_atc_h_v_7 = False
sh_atc_h_v_8 = False
sh_atc_h_v_9 = False
sh_atc_h_v_10 = False

# life
vite = 3
game_over = False
tempo_ultimo_danno = 0  
invulnerabilita_durata = 1000  

durata_shake = 0       
intensita_shake = 6   

font = pygame.font.SysFont(None, 30)
font_grande = pygame.font.SysFont(None, 50)

# Variabili del cerchio nate all'avvio per evitare il crash
p_x = 0
p_y = 0
rad = 0
kirk = False
kirk_h = False

# --- MODIFICA 2: Forza un primo disegno pulito prima del ciclo per evitare lo schermo nero ---
window.blit(bkg, (0, 0))
pygame.draw.rect(window, "red", player)
pygame.display.update()

COLOR_AVVISO = (71, 27, 24)

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
        pygame.draw.rect(window, COLOR_AVVISO, atck_1_disegno)
        
    if mostra_attacco2:
        atck_2_disegno = atck_1.move(shake_x, shake_y)
        pygame.draw.rect(window, "red", atck_2_disegno)

    if sh_atc3:
        atck_3_disegno = atck_2.move(shake_x, shake_y)
        pygame.draw.rect(window, COLOR_AVVISO, atck_3_disegno)

    if sh_atc3_h:
        atck_3_h_disegno = atck_2.move(shake_x, shake_y)  
        pygame.draw.rect(window, "red", atck_3_h_disegno) 

    if sh_atc3_t:
        atck_3_t_disegno = atck_3.move(shake_x, shake_y)
        pygame.draw.rect(window, COLOR_AVVISO, atck_3_t_disegno) 

    if sh_atc3_t_h:  
        atck_3_t_h_disegno = atck_3.move(shake_x, shake_y)
        pygame.draw.rect(window, "red", atck_3_t_h_disegno) 

    # Preavvisi Orizzontali (Scuro)
    if sh_atc_1: pygame.draw.rect(window, COLOR_AVVISO, atck_1.move(shake_x, shake_y))
    if sh_atc_2: pygame.draw.rect(window, COLOR_AVVISO, atck_2.move(shake_x, shake_y))
    if sh_atc_3: pygame.draw.rect(window, COLOR_AVVISO, atck_3.move(shake_x, shake_y))
    if sh_atc_4: pygame.draw.rect(window, COLOR_AVVISO, atck_4.move(shake_x, shake_y))
    if sh_atc_5: pygame.draw.rect(window, COLOR_AVVISO, atck_5.move(shake_x, shake_y))
    if sh_atc_6: pygame.draw.rect(window, COLOR_AVVISO, atck_6.move(shake_x, shake_y))
    # Preavvisi Verticali (Scuro)
    if sh_atc_v_1: pygame.draw.rect(window, COLOR_AVVISO, atck_1_v.move(shake_x, shake_y))
    if sh_atc_v_2: pygame.draw.rect(window, COLOR_AVVISO, atck_2_v.move(shake_x, shake_y))
    if sh_atc_v_3: pygame.draw.rect(window, COLOR_AVVISO, atck_3_v.move(shake_x, shake_y))
    if sh_atc_v_4: pygame.draw.rect(window, COLOR_AVVISO, atck_4_v.move(shake_x, shake_y))
    if sh_atc_v_5: pygame.draw.rect(window, COLOR_AVVISO, atck_5_v.move(shake_x, shake_y))
    if sh_atc_v_6: pygame.draw.rect(window, COLOR_AVVISO, atck_6_v.move(shake_x, shake_y))
    if sh_atc_v_7: pygame.draw.rect(window, COLOR_AVVISO, atck_7_v.move(shake_x, shake_y))
    if sh_atc_v_8: pygame.draw.rect(window, COLOR_AVVISO, atck_8_v.move(shake_x, shake_y))
    if sh_atc_v_9: pygame.draw.rect(window, COLOR_AVVISO, atck_9_v.move(shake_x, shake_y))
    if sh_atc_v_10: pygame.draw.rect(window, COLOR_AVVISO, atck_10_v.move(shake_x, shake_y))

    # Attacchi Orizzontali Attivi (Rosso Chiaro)
    if sh_atc_h_1: pygame.draw.rect(window, "red", atck_1.move(shake_x, shake_y))
    if sh_atc_h_2: pygame.draw.rect(window, "red", atck_2.move(shake_x, shake_y))
    if sh_atc_h_3: pygame.draw.rect(window, "red", atck_3.move(shake_x, shake_y))
    if sh_atc_h_4: pygame.draw.rect(window, "red", atck_4.move(shake_x, shake_y))
    if sh_atc_h_5: pygame.draw.rect(window, "red", atck_5.move(shake_x, shake_y))
    if sh_atc_h_6: pygame.draw.rect(window, "red", atck_6.move(shake_x, shake_y))
    # Attacchi Verticali Attivi (Rosso Chiaro)
    if sh_atc_h_v_1: pygame.draw.rect(window, "red", atck_1_v.move(shake_x, shake_y))
    if sh_atc_h_v_2: pygame.draw.rect(window, "red", atck_2_v.move(shake_x, shake_y))
    if sh_atc_h_v_3: pygame.draw.rect(window, "red", atck_3_v.move(shake_x, shake_y))
    if sh_atc_h_v_4: pygame.draw.rect(window, "red", atck_4_v.move(shake_x, shake_y))
    if sh_atc_h_v_5: pygame.draw.rect(window, "red", atck_5_v.move(shake_x, shake_y))
    if sh_atc_h_v_6: pygame.draw.rect(window, "red", atck_6_v.move(shake_x, shake_y))
    if sh_atc_h_v_7: pygame.draw.rect(window, "red", atck_7_v.move(shake_x, shake_y))
    if sh_atc_h_v_8: pygame.draw.rect(window, "red", atck_8_v.move(shake_x, shake_y))
    if sh_atc_h_v_9: pygame.draw.rect(window, "red", atck_9_v.move(shake_x, shake_y))
    if sh_atc_h_v_10: pygame.draw.rect(window, "red", atck_10_v.move(shake_x, shake_y))

    # Disegni dei Cerchi con lo Shake matematico corretto
    if kirk: pygame.draw.circle(window, COLOR_AVVISO, (p_x + shake_x, p_y + shake_y), rad, width=0)
    if kirk_h: pygame.draw.circle(window, "red", (p_x + shake_x, p_y + shake_y), rad, width=0)

    # Interfaccia grafica (UI)
    testo_vite = font.render(f"Vite: {vite}", True, "white")
    window.blit(testo_vite, (20, 20))

    if game_over:
        testo_game_over = font_grande.render("GAME OVER", True, "red")
        testo_restart = font.render("Premi SPAZIO per ricominciare", True, "white")
        window.blit(testo_game_over, (380, 230))
        window.blit(testo_restart, (330, 300))

    # damage
    # damage
    if not game_over:
        player_corrente = player_l if ss_l else player
        subisce_danno = False
        tempo_attuale = pygame.time.get_ticks()

        if tempo_attuale - tempo_ultimo_danno > invulnerabilita_durata:
            # 1. Attacchi della prima fase
            if mostra_attacco2 and player_corrente.colliderect(atck_1): subisce_danno = True
            elif sh_atc3_h and player_corrente.colliderect(atck_2): subisce_danno = True
            elif sh_atc3_t_h and player_corrente.colliderect(atck_3): subisce_danno = True
            
            # 2. Attacchi Orizzontali (Compresi quelli dell'evento s_12)
            elif sh_atc_h_1 and player_corrente.colliderect(atck_1): subisce_danno = True
            elif sh_atc_h_2 and player_corrente.colliderect(atck_2): subisce_danno = True
            elif sh_atc_h_3 and player_corrente.colliderect(atck_3): subisce_danno = True
            elif sh_atc_h_4 and player_corrente.colliderect(atck_4): subisce_danno = True
            elif sh_atc_h_5 and player_corrente.colliderect(atck_5): subisce_danno = True
            elif sh_atc_h_6 and player_corrente.colliderect(atck_6): subisce_danno = True
            
            # 3. Attacchi Verticali (Compresi quelli dell'evento s_12)
            elif sh_atc_h_v_1 and player_corrente.colliderect(atck_1_v): subisce_danno = True
            elif sh_atc_h_v_2 and player_corrente.colliderect(atck_2_v): subisce_danno = True
            elif sh_atc_h_v_3 and player_corrente.colliderect(atck_3_v): subisce_danno = True
            elif sh_atc_h_v_4 and player_corrente.colliderect(atck_4_v): subisce_danno = True
            elif sh_atc_h_v_5 and player_corrente.colliderect(atck_5_v): subisce_danno = True
            elif sh_atc_h_v_6 and player_corrente.colliderect(atck_6_v): subisce_danno = True
            elif sh_atc_h_v_7 and player_corrente.colliderect(atck_7_v): subisce_danno = True
            elif sh_atc_h_v_8 and player_corrente.colliderect(atck_8_v): subisce_danno = True
            elif sh_atc_h_v_9 and player_corrente.colliderect(atck_9_v): subisce_danno = True
            elif sh_atc_h_v_10 and player_corrente.colliderect(atck_10_v): subisce_danno = True

            # 4. Calcolo Danno Cerchio (Posizionato fuori dalla catena elif orizzontale/verticale)
            if kirk_h:
                centro_cerchio_x = p_x + shake_x
                centro_cerchio_y = p_y + shake_y
                
                dist_x = player_corrente.centerx - centro_cerchio_x
                dist_y = player_corrente.centery - centro_cerchio_y
                if (dist_x**2 + dist_y**2) < rad**2:
                    subisce_danno = True

        if subisce_danno:
            vite -= 1
            tempo_ultimo_danno = tempo_attuale  
            if vite <= 0:
                game_over = True
                pygame.mixer.music.stop()
                mostra_attacco1 = False
                mostra_attacco2 = False
                sh_atc3 = False
                sh_atc3_h = False
                sh_atc3_t = False
                sh_atc3_t_h = False
                sh_atc_1 = False
                sh_atc_2 = False
                sh_atc_3 = False
                sh_atc_4 = False
                sh_atc_5 = False
                sh_atc_6 = False
                sh_atc_v_1 = False
                sh_atc_v_2 = False
                sh_atc_v_3 = False
                sh_atc_v_4 = False
                sh_atc_v_5 = False
                sh_atc_v_6 = False
                sh_atc_v_7 = False
                sh_atc_v_8 = False
                sh_atc_v_9 = False
                sh_atc_v_10 = False

                sh_atc_h_1 = False
                sh_atc_h_2 = False
                sh_atc_h_3 = False
                sh_atc_h_4 = False
                sh_atc_h_5 = False
                sh_atc_h_6 = False
                sh_atc_h_v_1 = False
                sh_atc_h_v_2 = False
                sh_atc_h_v_3 = False
                sh_atc_h_v_4 = False
                sh_atc_h_v_5 = False
                sh_atc_h_v_6 = False
                sh_atc_h_v_7 = False
                sh_atc_h_v_8 = False
                sh_atc_h_v_9 = False
                sh_atc_h_v_10 = False
                kirk_h = False
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

    # Ciclo degli eventi di Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            exit()

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
                pygame.time.set_timer(s_atc, 500, loops=1)

            elif event.type == s_atc:
                sh_atc3 = True
                sh_atc3_t = True
                pygame.time.set_timer(s_atc_h, 500, loops=1)

            elif event.type == s_atc_h:
                sh_atc3 = False
                sh_atc3_t = False
                mostra_attacco1 = False  
                mostra_attacco2 = True
                sh_atc3_h = True    
                sh_atc3_t_h = True
                durata_shake = 10
                pygame.time.set_timer(s_atc_h_del, 700, loops=1)

            elif event.type == s_atc_h_del:
                mostra_attacco2 = False
                sh_atc3_h = False
                sh_atc3_t_h = False
                sh_atc_v_3 = True
                pygame.time.set_timer(s_1, 200, loops=1)

            elif event.type == s_1:
                sh_atc_v_4 = True
                pygame.time.set_timer(s_2, 200, loops=1)

            elif event.type == s_2:
                sh_atc_v_5 = True
                pygame.time.set_timer(s_3, 300, loops=1)
            elif event.type == s_3:
                sh_atc_v_6 = True
                sh_atc_v_7 = True
                sh_atc_v_8 = True
                pygame.time.set_timer(s_4, 500, loops=1)
            elif event.type == s_4:
                sh_atc_v_3 = False
                sh_atc_v_4 = False
                sh_atc_v_5 = False
                sh_atc_v_6 = False
                sh_atc_v_7 = False
                sh_atc_v_8 = False
                sh_atc_v_5 = False
                sh_atc_h_v_3 = True
                sh_atc_h_v_4 = True
                sh_atc_h_v_5 = True
                sh_atc_h_v_6 = True
                sh_atc_h_v_7 = True
                sh_atc_h_v_8 = True
                durata_shake = 6
                pygame.time.set_timer(s_5, 500, loops=1)
            elif event.type == s_5:
                sh_atc_h_v_3 = False
                sh_atc_h_v_5 = False
                sh_atc_h_v_8 = False
                sh_atc_1 = True
                sh_atc_3 = True
                sh_atc_5 = True
                pygame.time.set_timer(s_6, 1300, loops=1)
            elif event.type == s_6:
                sh_atc_1 = False
                sh_atc_3 = False
                sh_atc_5 = False
                sh_atc_h_1 = True
                sh_atc_h_3 = True
                sh_atc_h_5 = True
                durata_shake = 6
                pygame.time.set_timer(s_7, 500, loops=1)
            elif event.type == s_7:
                sh_atc_h_1 = False
                sh_atc_h_3 = False
                sh_atc_h_5 = False
                sh_atc_h_v_2 = False
                sh_atc_h_v_4 = False
                sh_atc_h_v_6 = False
                sh_atc_h_v_7 = False
                sh_atc_h_v_8 = False
                pygame.time.set_timer(s_8, 500, loops=1)
            elif event.type == s_8:
                p_x = 500
                p_y = 300
                rad = 100
                kirk = True
                pygame.time.set_timer(s_9, 500, loops=1)
            elif event.type == s_9:
                p_x = 500
                p_y = 300
                rad = 110
                kirk_h = True
                kirk = False
                durata_shake = 6
                pygame.time.set_timer(s_10, 500, loops=1)
            elif event.type == s_10:
                kirk_h = False
                pygame.time.set_timer(s_11, 500, loops=1)
            elif event.type == s_11:
                sh_atc_3 = True
                sh_atc_4 = True
                sh_atc_v_4 = True
                sh_atc_v_7 = True
                pygame.time.set_timer(s_12, 500, loops=1)
            elif event.type == s_12:
                sh_atc_h_3 = True
                sh_atc_h_4 = True
                sh_atc_h_v_4 = True
                sh_atc_h_v_7 = True
                sh_atc_3 = False
                sh_atc_4 = False
                sh_atc_v_4 = False
                sh_atc_v_7 = False
                durata_shake = 6
                p_x = 160
                p_y = 100
                rad = 90
                kirk = True
                pygame.time.set_timer(s_13, 500, loops=1)
            elif event.type == s_13:
                kirk_h = True
                kirk = False
                durata_shake = 6
                pygame.time.set_timer(s_14, 500, loops=1)
            elif event.type == s_14:
                sh_atc_6 = True
                sh_atc_v_4 = True
                sh_atc_v_5 = True
                sh_atc_v_6 = True
                pygame.time.set_timer(s_15, 500, loops=1)
            elif event.type == s_15:
                sh_atc_6 = False
                sh_atc_v_4 = False
                sh_atc_v_5 = False
                sh_atc_v_6 = False
                sh_atc_h_6 = True
                sh_atc_h_v_4 = True
                sh_atc_h_v_5 = True
                sh_atc_h_v_6 = True
                durata_shake = 6
                pygame.time.set_timer(s_16, 500, loops=1)
            elif event.type == s_16:
                sh_atc_h_6 = False
                sh_atc_h_v_4 = False
                sh_atc_h_v_5 = False
                sh_atc_h_v_6 = False
                kirk_h = False
                sh_atc_h_3 = False
                sh_atc_h_4 = False
                sh_atc_h_v_4 = False
                sh_atc_h_v_7 = False
                pygame.time.set_timer(s_17, 300, loops=1)
            elif event.type == s_17:
                sh_atc_v_10 = True
                pygame.time.set_timer(s_18, 300, loops=1)
            elif event.type == s_18:
                sh_atc_v_9 = True
                pygame.time.set_timer(s_19, 300, loops=1)
            elif event.type == s_19:
                sh_atc_v_8 = True
                pygame.time.set_timer(s_20, 300, loops=1)
            elif event.type == s_20:
                sh_atc_h_v_10 = True
                sh_atc_v_10 = False
                sh_atc_v_1 = True
                durata_shake = 6
                pygame.time.set_timer(s_21, 300, loops=1)
            elif event.type == s_21:
                sh_atc_h_v_9 = True
                sh_atc_v_9 = False
                sh_atc_v_2 = True
                durata_shake = 6
                pygame.time.set_timer(s_22, 300, loops=1)
            elif event.type == s_22:
                sh_atc_h_v_8 = True
                sh_atc_v_8 = False
                sh_atc_v_3 = True
                durata_shake = 6
                pygame.time.set_timer(s_23, 300, loops=1)
            elif event.type == s_23:
                sh_atc_h_v_1 = True
                sh_atc_v_1 = False
                sh_atc_1 = True
                durata_shake = 6
                pygame.time.set_timer(s_24, 300, loops=1)
            elif event.type == s_24:
                sh_atc_h_v_2 = True
                sh_atc_v_2 = False
                sh_atc_2 = True
                durata_shake = 6
                pygame.time.set_timer(s_25, 300, loops=1)
            elif event.type == s_25:
                sh_atc_h_v_3 = True
                sh_atc_v_3 = False
                sh_atc_6 = True
                durata_shake = 6
                pygame.time.set_timer(s_26, 300, loops=1)
            elif event.type == s_26:
                sh_atc_h_1 = True
                sh_atc_1 = False
                sh_atc_5 = True
                durata_shake = 6
                pygame.time.set_timer(s_27, 300, loops=1)
            elif event.type == s_27:
                sh_atc_h_2 = True
                sh_atc_2 = False
                durata_shake = 6
                pygame.time.set_timer(s_28, 300, loops=1)
            elif event.type == s_28:
                sh_atc_h_6 = True
                sh_atc_6 = False
                durata_shake = 6
                pygame.time.set_timer(s_29, 300, loops=1)
            elif event.type == s_29:
                sh_atc_h_5 = True
                sh_atc_5 = False
                durata_shake = 6
                pygame.time.set_timer(s_30, 300, loops=1)




        # Input pulsanti fissi (INVIO per avviare/resettare e SPAZIO per il Dash)
        if event.type == pygame.KEYDOWN:
            
            # --- TASTO INVIO: Avvia la sequenza o resetta il gioco ---
            if event.key == pygame.K_RETURN:
                if game_over:
                    vite = 3; game_over = False
                    player.x, player.y = 200, 300
                    player_l.x, player_l.y = 200, 300
                    mostra_attacco1 = mostra_attacco2 = False
                    sh_atc3 = sh_atc3_h = sh_atc3_t = sh_atc3_t_h = False
                    sh_atc_v_3 = sh_atc_v_4 = sh_atc_v_5 = sh_atc_v_6 = False
                    sh_atc_h_v_3 = sh_atc_h_v_4 = sh_atc_h_v_5 = sh_atc_h_v_6 = False
                    sh_kirk = sh_kirk_h = False; durata_shake = 0
                else:
                    if not mostra_attacco1 and not mostra_attacco2 and not sh_atc3 and not sh_atc3_h and not sh_atc3_t and not sh_atc3_t_h and not sh_atc_h_v_3 and not kirk_h:
                        mostra_attacco1 = True  
                        pygame.time.set_timer(EVENTO_CANCELLA_ATTACCO_1, 500, loops=1)
                        pygame.mixer.music.load("music/Creo_Crazy.mp3")
                        pygame.mixer.music.play(loops=0, start=80.0, fade_ms=100)

            # --- TASTO SPAZIO: Esegue il Dash ---
            elif event.key == pygame.K_SPACE and not game_over:
                if not s_done:
                    # 1. Controllo asse orizzontale (A o D)
                    if ss_l:
                        if s_l: # Guarda a SINISTRA
                            if player.x >= 200: player.x -= 200; player_l.x -= 200
                            else: player.x = 0; player_l.x = 0
                        else: # Guarda a DESTRA
                            if player.x + 200 <= 1000: player.x += 200; player_l.x += 200
                            else: player.x = 1000 - 25; player_l.x = 1000 - 25
                        s_done = True
                        # Fai partire il timer di ricarica solo se il dash è stato eseguito
                        pygame.time.set_timer(charge, 200, loops=1) 
                        
                    # 2. Controllo asse verticale (W o S)
                    elif ss_u:
                        if s_u: # Guarda SOPRA
                            if player.y >= 200: player.y -= 200; player_l.y -= 200
                            else: player.y = 0; player_l.y = 0
                        else: # Guarda SOTTO
                            if player.y + 200 <= 600: player.y += 200; player_l.y += 200
                            else: player.y = 600 - 25; player_l.y = 600 - 25
                        s_done = True
                        # Fai partire il timer di ricarica solo se il dash è stato eseguito
                        pygame.time.set_timer(charge, 200, loops=1)

        # --- GESTIONE TIMER DEL DASH (Spostato FUORI da KEYDOWN) ---
        if event.type == charge:
            s_done = False # Ora si ricarica correttamente dopo 200 ms!

                    

    
        

    if player.x > 1000:
        player.x = 1000
        player_l.x = 1000

    # --- MOVIMENTI CONTINUI (W, A, S, D) ---
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
