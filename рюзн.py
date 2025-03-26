import pygame

pygame.init()

WINDOW_SIZE = (1000, 600)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [BLACK, RED, GREEN, BLUE, WHITE]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Paint 3')
screen.fill(WHITE)

running = True
clock = pygame.time.Clock()
fps = 60

color = BLACK
shape = 'line'
width = 3

prev, cur = None, None

font = pygame.font.SysFont('Verdana', 15)

def draw_ui():
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_SIZE[0], 50))
    screen.blit(font.render(f'Mode: {shape}', True, BLACK), (10, 10))
    screen.blit(font.render(f'Width: {width}', True, BLACK), (310, 10))
    pygame.draw.rect(screen, color, (610, 10, 30, 30))
    
    for i, c in enumerate(COLORS):
        pygame.draw.rect(screen, c, (700 + i * 40, 10, 30, 30))
        pygame.draw.rect(screen, BLACK, (700 + i * 40, 10, 30, 30), 2)

draw_ui()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and width > 1:
                width -= 1
            if event.key == pygame.K_UP:
                width += 1
            if event.key == pygame.K_c:
                shape = 'circle'
            if event.key == pygame.K_r:
                shape = 'rectangle'
            if event.key == pygame.K_l:
                shape = 'line'
            if event.key == pygame.K_e:
                shape = 'eraser'

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            # Проверка нажатия на палитру
            for i, c in enumerate(COLORS):
                if 700 + i * 40 <= x <= 730 + i * 40 and 10 <= y <= 40:
                    color = c
            
            prev = event.pos
        
        if event.type == pygame.MOUSEMOTION and prev:
            cur = event.pos
            if shape == 'line':
                pygame.draw.line(screen, color, prev, cur, width)
            if shape == 'eraser':
                pygame.draw.line(screen, WHITE, prev, cur, width)
            prev = cur
        
        if event.type == pygame.MOUSEBUTTONUP:
            cur = event.pos
            if shape == 'circle':
                x = (prev[0] + cur[0]) // 2
                y = (prev[1] + cur[1]) // 2
                r = abs(prev[0] - cur[0]) // 2
                pygame.draw.circle(screen, color, (x, y), r, width)
            if shape == 'rectangle':
                x, y = min(prev[0], cur[0]), min(prev[1], cur[1])
                w, h = abs(prev[0] - cur[0]), abs(prev[1] - cur[1])
                pygame.draw.rect(screen, color, (x, y, w, h), width)
            prev = None
    
    draw_ui()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
