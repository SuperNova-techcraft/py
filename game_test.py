import pygame
from sys import exit


pygame.init()
window = pygame.display.set_mode((1000, 600))  #window size
pygame.display.set_caption("SN-  PyGame") #name on upbar
clock = pygame.time.Clock()
#(from x, from y, lumghezza, larcghezza)
player = pygame.Rect(200, 300, 20, 25)

while True:
    window.fill("#15191f")
    pygame.draw.rect(window, "red", player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #press the close button
            pygame.quit()
            exit()
    kes = pygame.key.get_pressed()
    if kes[pygame.K_w]:
        player .y -= 5
    if kes[pygame.K_s]:
            player .y += 5
    if kes[pygame.K_a]:
            player .x -= 5
    if kes[pygame.K_d]:
            player .x += 5

    pygame.display.update()
    clock.tick(60)  #fps