import pygame

FRAMERATE = 60
WIDTH, HEIGHT = 800, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dino but a Person (& snails)")

# simple surfaces
# test_surface = pygame.Surface((100, 200))
# test_surface.fill("red")

# images
sky_surf = pygame.image.load("./graphics/sky.png").convert()
ground_surf = pygame.image.load("./graphics/ground.png").convert()
# do convert_alpha if the image is rectanglish
snail_surf = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_x = 700
snail_height = 265
snail_vel = -7
snail_rect = snail_surf.get_rect(topleft=(snail_x, snail_height))

player_surf = pygame.image.load("./graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(60, 300))
player_gravity = 0

score = 0
last_increment_score = 50

# fonts
font = pygame.font.Font("./font/Pixeltype.ttf", 30)
enter_text = font.render("press enter to start the game", False, "black")

clock = pygame.time.Clock()
running = True
game_active = False

while running:
    clock.tick(FRAMERATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEMOTION  # if mouse is moved at all
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -18.5

        # better approach then pygame.key
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if not game_active:
                    game_active = True
                    score = 0
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -18.5

    # screen.blit(test_surface, (0, 0))
    # backdrop
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))

    # info
    score_text = font.render(f"score: {round(score)}", False, "red")
    score_rect = score_text.get_rect(topright=(WIDTH, 0))
    screen.blit(score_text, score_rect)
    if not game_active:
        screen.blit(enter_text, (300, 50))
        pygame.display.update()
        continue

    # draw module
    # pygame.draw.line(screen, "pink", (0, 0), pygame.mouse.get_pos(), 3)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom > 300:
        player_rect.bottom = 300

    # characters
    snail_rect.x += snail_vel
    if snail_rect.x < -100:
        snail_rect.topleft = (WIDTH, snail_height)
    screen.blit(snail_surf, snail_rect)

    screen.blit(player_surf, player_rect)
    if player_rect.colliderect(snail_rect):
        snail_rect.x = 700
        snail_vel = -7
        game_active = False

    # pygame.mouse.get_pressed()  # returns a tuple of bools stating if the mouse is left, scroll, or right clicked
    # pygame.mouse.get_pos()  # alternate way to get mouse position

    # keyboard works similarly
    # keys = pygame.key.get_pressed()  # returns a tuple (akshually class) of all key states
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    score += 0.1
    if score > last_increment_score:
        snail_vel -= 1
        last_increment_score += 50
    pygame.display.update()

pygame.quit()