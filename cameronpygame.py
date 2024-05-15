import pygame

#Initialize pygame
pygame.init()


# Game Window variables being declared
SCREEN_WIDTH = 1525
SCREEN_HEIGHT = 780
# seeting up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#setting up player
player = pygame.Rect((850, 700, 50, 50))
#seetting up coin
coin = pygame.Rect((750, 300, 20, 20))

# Game loop
run = True
while run:
    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 255, 255), player)

    pygame.draw.rect(screen, (0, 225, 225), coin)
    
   
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and player.left >0:
        player.move_ip(-2,0)
    
    
    if key[pygame.K_w] == True and player.top >0:
        player.move_ip(0,-2)
        
    if key[pygame.K_s] == True and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0,2)
        
    if key[pygame.K_d] == True and player.right < SCREEN_WIDTH:
        player.move_ip(2,0)
    
    
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()        
    
pygame.quit()