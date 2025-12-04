import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (retro green terminal style)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_SPEED = 3
PIPE_GAP = 200
PIPE_SPACING = 300

class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.width = 40
        self.height = 30
        
    def flap(self):
        self.velocity = FLAP_STRENGTH
        
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        
    def draw(self, screen, font):
        # ASCII bird art
        bird_art = [
            ">o)",
            "(_>"
        ]
        for i, line in enumerate(bird_art):
            text = font.render(line, True, GREEN)
            screen.blit(text, (self.x, self.y + i * 15))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(150, SCREEN_HEIGHT - 250)
        self.width = 60
        self.passed = False
        
    def update(self):
        self.x -= PIPE_SPEED
        
    def draw(self, screen, font):
        # Top pipe
        for y in range(0, self.gap_y, 20):
            pipe_char = "║" * 6
            text = font.render(pipe_char, True, DARK_GREEN)
            screen.blit(text, (self.x, y))
        
        # Bottom pipe
        for y in range(self.gap_y + PIPE_GAP, SCREEN_HEIGHT, 20):
            pipe_char = "║" * 6
            text = font.render(pipe_char, True, DARK_GREEN)
            screen.blit(text, (self.x, y))
            
    def get_rects(self):
        top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        bottom_rect = pygame.Rect(self.x, self.gap_y + PIPE_GAP, self.width, SCREEN_HEIGHT)
        return [top_rect, bottom_rect]
    
    def off_screen(self):
        return self.x < -self.width

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("ASCII Flappy Bird")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        self.big_font = pygame.font.Font(None, 72)
        self.reset()
        
    def reset(self):
        self.bird = Bird()
        self.pipes = [Pipe(SCREEN_WIDTH + i * PIPE_SPACING) for i in range(3)]
        self.score = 0
        self.game_over = False
        self.game_started = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_started:
                        self.game_started = True
                    if self.game_over:
                        self.reset()
                    else:
                        self.bird.flap()
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def update(self):
        if not self.game_started or self.game_over:
            return
            
        # Update bird
        self.bird.update()
        
        # Check if bird hit ground or ceiling
        if self.bird.y > SCREEN_HEIGHT - 30 or self.bird.y < 0:
            self.game_over = True
            
        # Update pipes
        for pipe in self.pipes:
            pipe.update()
            
            # Check collision
            bird_rect = self.bird.get_rect()
            for pipe_rect in pipe.get_rects():
                if bird_rect.colliderect(pipe_rect):
                    self.game_over = True
                    
            # Check if passed pipe
            if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                pipe.passed = True
                self.score += 1
                
            # Remove off-screen pipes and add new ones
            if pipe.off_screen():
                self.pipes.remove(pipe)
                self.pipes.append(Pipe(self.pipes[-1].x + PIPE_SPACING))
    
    def draw(self):
        # Fill screen with black
        self.screen.fill(BLACK)
        
        # Draw decorative ASCII border
        border = "=" * 100
        border_text = self.font.render(border, True, DARK_GREEN)
        self.screen.blit(border_text, (0, SCREEN_HEIGHT - 25))
        
        # Draw pipes
        for pipe in self.pipes:
            pipe.draw(self.screen, self.font)
        
        # Draw bird
        self.bird.draw(self.screen, self.font)
        
        # Draw score
        score_text = self.font.render(f"SCORE: {self.score}", True, GREEN)
        self.screen.blit(score_text, (10, 10))
        
        # Draw start message
        if not self.game_started:
            start_text = self.big_font.render("PRESS SPACE", True, GREEN)
            text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(start_text, text_rect)
            
            subtitle = self.font.render("TO START", True, DARK_GREEN)
            sub_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
            self.screen.blit(subtitle, sub_rect)
        
        # Draw game over
        if self.game_over:
            game_over_text = self.big_font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
            
            restart_text = self.font.render("PRESS SPACE TO RESTART", True, GREEN)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
