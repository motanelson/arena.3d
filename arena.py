
import pygame
import math

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boneco Anatômico 3D Simulado")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Posição inicial do boneco
x = 0
z = 10  # Controle da "profundidade"
z_min = 5
z_max = 50
scale_factor = 10

# Função para desenhar o boneco com base na profundidade (z)
def draw_boneco(surface, center_x, center_y, scale):
    # Cabeça
    pygame.draw.circle(surface, WHITE, (center_x, center_y - int(50 * scale)), int(10 * scale))

    # Tronco
    pygame.draw.line(
        surface, WHITE,
        (center_x, center_y - int(40 * scale)),
        (center_x, center_y + int(20 * scale)),
        int(2 * scale)
    )

    # Braços
    arm_length = int(30 * scale)
    pygame.draw.line(
        surface, WHITE,
        (center_x, center_y - int(30 * scale)),
        (center_x - arm_length, center_y),
        int(2 * scale)
    )
    pygame.draw.line(
        surface, WHITE,
        (center_x, center_y - int(30 * scale)),
        (center_x + arm_length, center_y),
        int(2 * scale)
    )

    # Pernas
    leg_length = int(40 * scale)
    pygame.draw.line(
        surface, WHITE,
        (center_x, center_y + int(20 * scale)),
        (center_x - int(15 * scale), center_y + int(20 * scale) + leg_length),
        int(2 * scale)
    )
    pygame.draw.line(
        surface, WHITE,
        (center_x, center_y + int(20 * scale)),
        (center_x + int(15 * scale), center_y + int(20 * scale) + leg_length),
        int(2 * scale)
    )

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar entrada do teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x =  x - 1
        
    if keys[pygame.K_RIGHT]:
        x = x + 1
    if keys[pygame.K_UP]:
        z = min(z_max, z + 1)
    if keys[pygame.K_DOWN]:
        z = max(z_min, z - 1)
    if x<-(z):
        x=-(z)
    if x>z:
        x=z
    # Calcular parâmetros com base em z
    scale = 1 / z * scale_factor
    center_x = screen_width // 2 + int(x * scale * 20)
    center_y = screen_height // 2 + int(z * scale * 10)

    # Limpar tela
    screen.fill(BLACK)

    # Desenhar o boneco
    draw_boneco(screen, center_x, center_y, scale)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    clock.tick(60)

# Sair do Pygame
pygame.quit()
