import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("My Game")
img_01 = pygame.image.load("./Images/football.png")
screen.fill((255, 255, 255))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(img_01, (0, 0))
    pygame.display.update()
pygame.quit()
