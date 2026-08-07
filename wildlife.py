import pygame
pygame.init()
screen = pygame.display.set_mode((500,400))
title = pygame.display.set_caption('Gecko')
image_bg= pygame.transform.scale(pygame.image.load('rare-leopard-geckos.png').convert(),(500,400))
image_c= pygame.transform.scale(pygame.image.load('gecko_tail_regrowth_process.png').convert_alpha(),(200,100))
rect= image_c.get_rect(center=(500//2,400//2))
txt= pygame.font.Font(None,36).render('Geckos have sticky fingers.', True, pygame.Color('black'))
smt=txt.get_rect(center=(250,200 + 110))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(image_bg, (0,0))
    screen.blit(image_c, rect)
    screen.blit(txt, smt)
    pygame.display.flip()