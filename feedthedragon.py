import pygame, random

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
player_lives = PLAYER_STARTING_LIVES
Coin_velocity = COIN_EXCELERATION

GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(Attack.Graffiti.ttf , 32)

score_text = font.render("Score: " + str("score), True, GREEN, DARK_GREEN)"
title_rect = score_text.get_rect()
score_rect.topleft = (10, 10))

render_font = "Feed the Dragon", True, GREEN, WHITE
title_rect.centerx = WINDOW_WIDTH / 2
title_rect.y = 10
lives_text = ("Lives: str(player_lives), True, GREEN, DARKGREEN)"
game_over_text = "GAME_OVER"
game_over_rect = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

coin_sound = pygame.mixer.sound("coin_sound.wav")
miss_sound = pygame.mixer.sound("miss_sound.wav")
coin_sound.set_volume(0.2)
miss_sound.set.volume(0.1)
pygame.mixer.music.load("ftd_background_music.wav")


player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

BUFFER_IMAGE = 10

rect_location: x = WINDOW_WIDTH + BUFFER_DISTANCE
rect_location: y = random.randint(64, WINDOW_HEIGHT - 32)
pygame.mixer.music.play(loops: -1, start: 0.0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
display_surface.blit(score_text, lives_text)
display_surface.blit(title_text, title_rect)
display_surface.blit(lives_text, lives_rect)
display_surface.blit(player_image, player_rect)
display_surface.blit(coin_image, coin_rect)
coin_rect.y = random.randint ( 64, WINDOW_HEIGHT - 32)

pygame.draw.line(display.surface, WHITE,(0, 64), WINDOW_WIDTH, 64), 2)

    score_text = font.render("Score: " + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives: " + str(lives), True, GREEN, DARK_GREEN)

if player_lives == 0
    display_surface.blit(game_over_text, game_over_rect)
    display_surface.blit(continue_text, continuue_rect)
    pygame.display.update()

    pygame.mixer.music.stop()
    is_paused = True
    while is_paused
        for event in pygame.event.get()
            if event.type == pygame.KEYDOWN:
                is_paused = false
if event.type == pygame.QUIT:


keys = pygame.key.get.pressed
if keys[pygame.K_UP]
    player_rect.y -= PLAYER_VELOCITY < WINDOW_HEIGHT
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_VELOCITY < WINDOW_HEIGHT

        if coin_rect.x < 0
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + buffer_zone
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
        else:
        coin_rect.x -= coin_velocity

        if player_rect.colliderect(coin_rect)
            score += 1
            coin_sound.play()

            COIN_STARTING_VELOCITY =

display_surface.fill(BLACK))
clock.tick(FPS)

pygame.quit()