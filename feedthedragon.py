import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

FPS = 60
clock = pygame.time.Clock()
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_EXCELERATION = 0.5

score = 0
player_lives = (PLAYER_STARTING_LIVES)
Coin_velocity = (COIN_EXCELERATION)

GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(Attack.Graffiti.ttf , 32)

score_text = font.render("Score: " + str("score), True, GREEN, DARK_GREEN)"
title_rect = score_text.get_rect()
score rect.topleft = (10, 10))

render font = "Feed the Dragon", True, GREEN, WHITE
title_rect.centerx = WINDOW_WIDTH / 2
title_rect.y = 10
lives_text = ("Lives: str(player_lives), True, GREEN, DARKGREEN)"
game_over_text =
game_over_rect = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render("Lives: " + str(lives), True, GREEN, DARKGREEN)

display_surface.fill(BLACK))

pygame.quit()