import os
import pygame

pygame.init()

s_w, s_h = 600, 600
screen = pygame.display.set_mode((s_w, s_h), pygame.RESIZABLE)
pygame.display.set_caption("WorldwileMusic")

icon_path = r"C:\Users\USER\Desktop\images.jpeg"
if os.path.exists(icon_path):
    icon_image = pygame.image.load(icon_path)
    pygame.display.set_icon(icon_image)

music_folder = r"C:\Users\USER\Desktop\mumu"

playlist = [
    "Zdravstvujj_nebo_v_oblakakh_Zdravstvujj_yunost_v_sapogakh_Propadi_moya_toska_Vot_on_ya_privet_vojjska_JEkh_relsy_poezda_Kak_ya_popal_syuda_Zdes_ne_t_-_Soldaty_75735308.mp3",
    "Serani_Poji_-_Pipo_Pipo_76462824.mp3"
]

current_music = 0
is_playing = False

def play_music(index):
    pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_music
    current_music = (current_music + 1) % len(playlist)
    play_music(current_music)

def prev_track():
    global current_music
    current_music = (current_music - 1) % len(playlist)
    play_music(current_music)

font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

running = True
while running:
    screen.fill((0, 0, 0))
    
    instructions = [
        "hehehehe mp3"
    ]
    
    y_offset = 200
    for line in instructions:
        text_surface = font.render(line, True, text_color)
        screen.blit(text_surface, (50, y_offset))
        y_offset += 40

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if not is_playing:
                    play_music(current_music)
                    is_playing = True
                else:
                    stop_music()
                    is_playing = False
            elif event.key == pygame.K_RIGHT: 
                next_track()
            elif event.key == pygame.K_LEFT:   
                prev_track()

pygame.quit()
