import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 80
OBSTACLE_WIDTH = 60
OBSTACLE_HEIGHT = 60
ROAD_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("2D Car Racing")
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.x = WINDOW_WIDTH // 2 - self.width // 2
        self.y = WINDOW_HEIGHT - self.height - 20
        self.speed = 8
        self.score = 0
        
        # Create a simple car rectangle
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(RED)
    
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WINDOW_WIDTH - self.width:
            self.x += self.speed
    
    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))

class Obstacle:
    def __init__(self):
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.x = random.randint(0, WINDOW_WIDTH - self.width)
        self.y = -self.height
        self.speed = ROAD_SPEED
        
        # Create a simple obstacle rectangle
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(GREEN)
    
    def move(self):
        self.y += self.speed
        return self.y > WINDOW_HEIGHT
    
    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))
    
    def collides_with(self, player):
        return (self.x < player.x + player.width and
                self.x + self.width > player.x and
                self.y < player.y + player.height and
                self.y + self.height > player.y)

def main():
    player = Player()
    obstacles = []
    obstacle_spawn_timer = 0
    game_over = False
    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE:
                    # Reset game
                    player = Player()
                    obstacles = []
                    obstacle_spawn_timer = 0
                    game_over = False
                    score = 0

        if not game_over:
            # Handle player movement
            keys = pygame.key.get_pressed()
            player.move(keys)

            # Spawn obstacles
            obstacle_spawn_timer += 1
            if obstacle_spawn_timer >= FPS:
                obstacles.append(Obstacle())
                obstacle_spawn_timer = 0

            # Update obstacles and check collisions
            for obstacle in obstacles[:]:
                if obstacle.move():
                    obstacles.remove(obstacle)
                    score += 1
                elif obstacle.collides_with(player):
                    game_over = True

        # Draw everything
        screen.fill(BLACK)
        
        # Draw road lines
        road_line_y = (pygame.time.get_ticks() * ROAD_SPEED) % WINDOW_HEIGHT
        for y in range(int(-road_line_y), WINDOW_HEIGHT, 100):
            pygame.draw.rect(screen, WHITE, (WINDOW_WIDTH//2 - 5, y, 10, 50))

        player.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render("Game Over! Press SPACE to restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            screen.blit(game_over_text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()