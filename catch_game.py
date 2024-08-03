import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catch the Falling Objects')

# Player properties
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 10

# Object properties
object_size = 50
object_pos = [random.randint(0, SCREEN_WIDTH - object_size), 0]
object_speed = 10

# Score
score = 0
font = pygame.font.SysFont("monospace", 35)

# Game loop control
game_over = False
clock = pygame.time.Clock()

def detect_collision(player_pos, object_pos):
    px, py = player_pos
    ox, oy = object_pos
    if (ox >= px and ox < (px + player_size)) or (px >= ox and px < (ox + object_size)):
        if (oy >= py and oy < (py + player_size)) or (py >= oy and py < (oy + object_size)):
            return True
    return False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed

    screen.fill(BLACK)

    object_pos[1] += object_speed
    if object_pos[1] > SCREEN_HEIGHT:
        object_pos = [random.randint(0, SCREEN_WIDTH - object_size), 0]
        score -= 1

    if detect_collision(player_pos, object_pos):
        object_pos = [random.randint(0, SCREEN_WIDTH - object_size), 0]
        score += 1

    pygame.draw.rect(screen, RED, (object_pos[0], object_pos[1], object_size, object_size))
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    score_text = "Score: {}".format(score)
    label = font.render(score_text, 1, WHITE)
    screen.blit(label, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 40))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
