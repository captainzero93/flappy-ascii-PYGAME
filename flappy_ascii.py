import pygame
import random
import sys
import numpy as np

# Initialize Pygame
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (retro green terminal style)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_SPEED = 3
PIPE_GAP = 200
PIPE_SPACING = 300

# Sound generation functions
def generate_flap_sound():
    """Generate a quick swoosh sound for flapping"""
    sample_rate = 22050
    duration = 0.1
    frequency = 300
    
    # Generate samples
    samples = np.arange(int(duration * sample_rate))
    # Create a quick frequency sweep down
    freqs = np.linspace(frequency, frequency * 0.5, len(samples))
    waveform = np.sin(2 * np.pi * freqs * samples / sample_rate)
    
    # Apply envelope to avoid clicks
    envelope = np.exp(-samples / (sample_rate * 0.05))
    waveform = waveform * envelope
    
    # Convert to 16-bit
    waveform = np.int16(waveform * 32767 * 0.3)
    
    # Make stereo
    stereo_waveform = np.column_stack((waveform, waveform))
    
    return pygame.sndarray.make_sound(stereo_waveform)

def generate_coin_sound():
    """Generate a pleasant coin collection sound"""
    sample_rate = 22050
    duration = 0.2
    
    # Two tone sound (like a coin)
    freq1 = 800
    freq2 = 1200
    
    samples = np.arange(int(duration * sample_rate))
    
    # First tone
    wave1 = np.sin(2 * np.pi * freq1 * samples / sample_rate)
    # Second tone (slightly delayed)
    wave2 = np.sin(2 * np.pi * freq2 * samples / sample_rate)
    
    # Combine with delay
    waveform = wave1 * 0.5
    delay_samples = int(0.05 * sample_rate)
    waveform[delay_samples:] += wave2[:len(waveform)-delay_samples] * 0.5
    
    # Apply envelope
    envelope = np.exp(-samples / (sample_rate * 0.1))
    waveform = waveform * envelope
    
    # Convert to 16-bit
    waveform = np.int16(waveform * 32767 * 0.4)
    
    # Make stereo
    stereo_waveform = np.column_stack((waveform, waveform))
    
    return pygame.sndarray.make_sound(stereo_waveform)

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

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.collected = False
        self.angle = 0  # For spinning animation
        
    def update(self):
        self.x -= PIPE_SPEED
        self.angle += 5  # Spin effect
        
    def draw(self, screen, font):
        if not self.collected:
            # ASCII coin with spinning effect
            if (self.angle // 30) % 2 == 0:
                coin_char = "($)"
            else:
                coin_char = "[§]"
            text = font.render(coin_char, True, YELLOW)
            screen.blit(text, (self.x, self.y))
            
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def off_screen(self):
        return self.x < -self.width

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(150, SCREEN_HEIGHT - 250)
        self.width = 60
        self.passed = False
        # Create coin in the middle of the gap
        self.coin = Coin(x + self.width // 2 - 15, self.gap_y + PIPE_GAP // 2 - 15)
        
    def update(self):
        self.x -= PIPE_SPEED
        if self.coin:
            self.coin.update()
        
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
        
        # Draw coin
        if self.coin:
            self.coin.draw(screen, font)
            
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
        
        # Generate sounds
        print("Generating sounds...")
        self.flap_sound = generate_flap_sound()
        self.coin_sound = generate_coin_sound()
        print("Sounds ready!")
        
        self.reset()
        
    def reset(self):
        self.bird = Bird()
        self.pipes = [Pipe(SCREEN_WIDTH + i * PIPE_SPACING) for i in range(3)]
        self.score = 0
        self.coins = 0
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
                        self.flap_sound.play()  # Play flap sound
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
            
            # Check coin collection
            if pipe.coin and not pipe.coin.collected:
                bird_rect = self.bird.get_rect()
                coin_rect = pipe.coin.get_rect()
                if bird_rect.colliderect(coin_rect):
                    pipe.coin.collected = True
                    self.coins += 1
                    self.coin_sound.play()  # Play coin sound
            
            # Check collision with pipes
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
        
        # Draw pipes (and coins)
        for pipe in self.pipes:
            pipe.draw(self.screen, self.font)
        
        # Draw bird
        self.bird.draw(self.screen, self.font)
        
        # Draw score
        score_text = self.font.render(f"SCORE: {self.score}", True, GREEN)
        self.screen.blit(score_text, (10, 10))
        
        # Draw coins
        coins_text = self.font.render(f"COINS: {self.coins}", True, YELLOW)
        self.screen.blit(coins_text, (10, 40))
        
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
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
            self.screen.blit(game_over_text, text_rect)
            
            final_score = self.font.render(f"Score: {self.score}  Coins: {self.coins}", True, GREEN)
            score_rect = final_score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            self.screen.blit(final_score, score_rect)
            
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
