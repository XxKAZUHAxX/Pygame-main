import pygame 
import os 
   
pygame.init()
screen_width = 1280
screen_height = 720
game_screen = pygame.display.set_mode((screen_width, screen_height))
# white color 
color = (255,255,255) 
# light shade of the button 
color_light = (170,170,170) 
# dark shade of the button 
color_dark = (100,100,100) 
# stores the width of the 
# screen into a variable 
width = game_screen.get_width() 
# stores the height of the 
# screen into a variable 
height = game_screen.get_height() 
# defining a font 
smallfont = pygame.font.SysFont('Arial',36) 
# rendering a text written in 
# this font 
text = smallfont.render('quit' , True , color) 
text2 = smallfont.render('start', True, color)
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
        #checks if a mouse is clicked 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            #set area where game will quit if mouse is clicked here
            if width/3+100 <= mouse[0] <= width/3+250 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit()
            #set area where game will start if mouse is clicked here
            if width/3+100 <= mouse[0] <= width/3+250 and height/2-90 <= mouse[1] <= height/2-50: 
                pygame.quit() #palagay ng code para magstart, palitan nalang yung .quit   
    # fills the screen with a color 
    game_screen.fill((200,200,200)) 
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if width/3+100 <= mouse[0] <= width/3+250 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(game_screen,color_light,[width/3+100,height/2,150,40]) 
        pygame.draw.rect(game_screen,color_dark,[width/3+100,height/2-90,150,40])
    elif width/3+100 <= mouse[0] <= width/3+250 and height/2-90 <= mouse[1] <= height/2-50:
        pygame.draw.rect(game_screen,color_light,[width/3+100,height/2-90,150,40])
        pygame.draw.rect(game_screen,color_dark,[width/3+100,height/2,150,40])
    else: 
        pygame.draw.rect(game_screen,color_dark,[width/3+100,height/2,150,40])
        pygame.draw.rect(game_screen,color_dark,[width/3+100,height/2-90,150,40])
    # superimposing the text onto our button 
    game_screen.blit(text , (width/3+150,height/2)) 
    game_screen.blit(text2, (width/3+145,height/2-90))
    # updates the frames of the game 
    pygame.display.update() 