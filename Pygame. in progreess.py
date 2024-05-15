import pygame
import random

def game():
    # Initialize pygame
    pygame.init()

    # Game Window variables being declared
    SCREEN_WIDTH = 1525
    SCREEN_HEIGHT = 780

    # Setting up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ghost Chase")

    # Setting up player
    player = pygame.Rect(850, 700, 50, 50)

    # Setting up coin
    coin = pygame.Rect(random.randint(10, SCREEN_WIDTH - 30), random.randint(10, SCREEN_HEIGHT - 30), 20, 20)

    # Ghost enemy setup
    ghost = pygame.Rect(200, 200, 30, 50)

    # Colors and fonts
    font40 = pygame.font.SysFont(None, 40)
    white = (255, 255, 255)

    # Spawn coin function
    def spawn_coin():
        coin.x = random.randint(10, SCREEN_WIDTH - 30)
        coin.y = random.randint(10, SCREEN_HEIGHT - 30)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # Game loop
    run = True
    ghost_move_delay = 10  # Delay between each ghost movement
    ghost_move_counter = 0  # Counter to keep track of ghost movements
    while run:
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), player)
        pygame.draw.rect(screen, (0, 225, 225), coin)
        pygame.draw.rect(screen, (200, 200, 200), ghost)

        # Movement handling
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.left > 0:
            player.x -= 2
        if key[pygame.K_w] and player.top > 0:
            player.y -= 2
        if key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
            player.y += 2
        if key[pygame.K_d] and player.right < SCREEN_WIDTH:
            player.x += 2

        # Ghost chasing with delay
        ghost_move_counter += 1
        if ghost_move_counter >= ghost_move_delay:
            if player.x < ghost.x:
                ghost.x -= 1
            elif player.x > ghost.x:
                ghost.x += 1
            if player.y < ghost.y:
                ghost.y -= 1
            elif player.y > ghost.y:
                ghost.y += 1
            ghost_move_counter = 0  # Reset the counter after movement

        # Check for player collision with ghost
        if player.colliderect(ghost):
            draw_text('Game Over', font40, white, 600, 350)
            pygame.display.update()
            pygame.time.delay(2000)
            run = False

        # Check for player collision with coin
        if player.colliderect(coin):
            spawn_coin()

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

game()

