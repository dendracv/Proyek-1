import pygame
import random
import sys

# 1. Inisialisasi Pygame
pygame.init()

# 2. Pengaturan Layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Apples!")

# 3. Warna (RGB)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (34, 139, 34)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# 4. Pengaturan FPS (Frames Per Second)
clock = pygame.time.Clock()
FPS = 60

# 5. Atribut Pemain (Keranjang)
basket_width = 100
basket_height = 20
basket_x = (SCREEN_WIDTH - basket_width) // 2
basket_y = SCREEN_HEIGHT - basket_height - 10
basket_speed = 10

# 6. Atribut Apel
apple_size = 20
apple_x = random.randint(0, SCREEN_WIDTH - apple_size)
apple_y = -apple_size
apple_speed = 5

# 7. Skor dan Game State
score = 0
font = pygame.font.SysFont("Arial", 30)
game_over = False

def show_score():
    score_text = font.render(f"Skor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def show_game_over():
    over_text = font.render("GAME OVER! Tekan R untuk Main Lagi atau Q untuk Keluar", True, RED)
    text_rect = over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(over_text, text_rect)

# 8. Loop Utama Game
while True:
    screen.fill(BLUE)  # Warna background langit biru

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Input Keyboard
    keys = pygame.key.get_pressed()
    
    if not game_over:
        # Gerakan Keranjang
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
            basket_x += basket_speed

        # Logika Gerakan Apel
        apple_y += apple_speed

        # Deteksi Tabrakan (Keranjang Menangkap Apel)
        if (basket_y < apple_y + apple_size < basket_y + basket_height) and \
           (basket_x < apple_x < basket_x + basket_width or basket_x < apple_x + apple_size < basket_x + basket_width):
            score += 1
            apple_x = random.randint(0, SCREEN_WIDTH - apple_size)
            apple_y = -apple_size
            # Tingkatkan kecepatan setiap kelipatan 5 skor agar lebih menantang
            if score % 5 == 0:
                apple_speed += 1

        # Jika Apel Lolos ke Bawah Layar
        if apple_y > SCREEN_HEIGHT:
            game_over = True

    else:
        # Pilihan saat Game Over
        show_game_over()
        if keys[pygame.K_r]:  # Reset Game
            game_over = False
            score = 0
            apple_speed = 5
            apple_y = -apple_size
            apple_x = random.randint(0, SCREEN_WIDTH - apple_size)
            basket_x = (SCREEN_WIDTH - basket_width) // 2
        if keys[pygame.K_q]:  # Keluar
            pygame.quit()
            sys.exit()

    # Gambar Objek ke Layar
    if not game_over:
        # Gambar Keranjang (Kotak Hijau)
        pygame.draw.rect(screen, GREEN, (basket_x, basket_y, basket_width, basket_height))
        # Gambar Apel (Kotak Merah)
        pygame.draw.rect(screen, RED, (apple_x, apple_y, apple_size, apple_size))
        show_score()

    pygame.display.update()
    clock.tick(FPS)
