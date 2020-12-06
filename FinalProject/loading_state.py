import random
import gfw
from pico2d import *
import main_state
import title_state
from gobj import res

canvas_width = main_state.canvas_width
canvas_height = main_state.canvas_height

center_x = canvas_width // 2
center_y = canvas_height // 2

def enter():
    global back, bg, fg, index, file, w, h
    back = gfw.image.load(res('loading.png'))
    bg = gfw.image.load(res('progress_bg.png'))
    fg = gfw.image.load(res('progress_fg.png'))
    index = 0

    global font, display
    font = gfw.font.load(res('ENCR10B.TTF'), 30)
    display = ''

    global frame_interval
    frame_interval = gfw.frame_interval
    gfw.frame_interval = 0
    w = random.randint(0,3)
    h = random.randint(0,11)

def exit():
    global back, bg, fg
    gfw.image.unload(res('loading.jpg'))
    gfw.image.unload(res('progress_bg.png'))
    gfw.image.unload(res('progress_fg.png'))
    del back
    del bg
    del fg

    global frame_interval
    gfw.frame_interval = frame_interval

def update():
    global index, display
    image_count = len(IMAGE_FILES)
    font_count = len(FONT_PAIRS)
    if index < image_count:
        file = IMAGE_FILES[index]
        gfw.image.load(file)
        display = file
    elif index - image_count < font_count:
        file, size = FONT_PAIRS[index - image_count]
        gfw.font.load(file, size)
        display = '%s %dpt' % (file, size)
    else:
        gfw.change(title_state)
        return
    index += 1

def draw():
    back.clip_draw_to_origin(0+256*w, 20+192*h, 256, 192, 0, 0, 1000, 900)
    image_count = len(IMAGE_FILES)
    font_count = len(FONT_PAIRS)
    progress = index / (image_count + font_count)
    draw_progress(center_x, 300, 800, progress)

    global display
    font.draw(300, 250, display)
    font.draw(300, 350, '%.1f%%' % (progress * 100))

def draw_progress(x, y, width, rate):
    l = x - width // 2
    b = y - bg.h // 2
    draw_3(bg, l, b, width, 3)
    draw_3(fg, l, b, round(width * rate), 3)

def draw_3(img, l, b, width, edge):
    img.clip_draw_to_origin(0, 0, edge, img.h, l, b, edge, img.h)
    img.clip_draw_to_origin(edge, 0, img.w - 2 * edge, img.h, l+edge, b, width - 2 * edge, img.h)
    img.clip_draw_to_origin(img.w - edge, 0, edge, img.h, l+width-edge, b, edge, img.h)

def handle_event(e):
    global unit
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

IMAGE_FILES = [
    "res/background.jpg",
    "res/monsterfiles/Bulbasaur/Dead (1).png",
    "res/monsterfiles/Bulbasaur/Idle (1).png",
    "res/monsterfiles/Bulbasaur/Idle (2).png",
    "res/monsterfiles/Bulbasaur/Idle (3).png",
    "res/monsterfiles/Bulbasaur/Walk (1).png",
    "res/monsterfiles/Bulbasaur/Walk (2).png",
    "res/monsterfiles/Bulbasaur/Walk (3).png",
    "res/monsterfiles/Bulbasaur/Walk (4).png",
    "res/monsterfiles/Bulbasaur/Walk (5).png",
    "res/monsterfiles/Bulbasaur/Walk (6).png",
    "res/monsterfiles/Bulbasaur/Walk (7).png",
    "res/monsterfiles/Ivysaur/Dead (1).png",
    "res/monsterfiles/Ivysaur/Idle (1).png",
    "res/monsterfiles/Ivysaur/Idle (2).png",
    "res/monsterfiles/Ivysaur/Idle (3).png",
    "res/monsterfiles/Ivysaur/Walk (1).png",
    "res/monsterfiles/Ivysaur/Walk (2).png",
    "res/monsterfiles/Ivysaur/Walk (3).png",
    "res/monsterfiles/Ivysaur/Walk (4).png",
    "res/monsterfiles/Ivysaur/Walk (5).png",
    "res/monsterfiles/Ivysaur/Walk (6).png",
    "res/monsterfiles/Venusaur/Dead (1).png",
    "res/monsterfiles/Venusaur/Idle (1).png",
    "res/monsterfiles/Venusaur/Idle (2).png",
    "res/monsterfiles/Venusaur/Idle (3).png",
    "res/monsterfiles/Venusaur/Walk (1).png",
    "res/monsterfiles/Venusaur/Walk (2).png",
    "res/monsterfiles/Venusaur/Walk (3).png",
    "res/monsterfiles/Venusaur/Walk (4).png",
    "res/monsterfiles/Venusaur/Walk (5).png",
    "res/monsterfiles/Charmander/Dead (1).png",
    "res/monsterfiles/Charmander/Idle (1).png",
    "res/monsterfiles/Charmander/Idle (2).png",
    "res/monsterfiles/Charmander/Idle (3).png",
    "res/monsterfiles/Charmander/Walk (1).png",
    "res/monsterfiles/Charmander/Walk (2).png",
    "res/monsterfiles/Charmander/Walk (3).png",
    "res/monsterfiles/Charmander/Walk (4).png",
    "res/monsterfiles/Charmander/Walk (5).png",
    "res/monsterfiles/Charmander/Walk (6).png",
    "res/monsterfiles/Charmeleon/Dead (1).png",
    "res/monsterfiles/Charmeleon/Idle (1).png",
    "res/monsterfiles/Charmeleon/Idle (2).png",
    "res/monsterfiles/Charmeleon/Idle (3).png",
    "res/monsterfiles/Charmeleon/Idle (4).png",
    "res/monsterfiles/Charmeleon/Idle (5).png",
    "res/monsterfiles/Charmeleon/Idle (6).png",
    "res/monsterfiles/Charmeleon/Idle (7).png",
    "res/monsterfiles/Charmeleon/Walk (1).png",
    "res/monsterfiles/Charmeleon/Walk (2).png",
    "res/monsterfiles/Charmeleon/Walk (3).png",
    "res/monsterfiles/Charmeleon/Walk (4).png",
    "res/monsterfiles/Charmeleon/Walk (5).png",
    "res/monsterfiles/Charmeleon/Walk (6).png",
    "res/monsterfiles/Charmeleon/Walk (7).png",
    "res/monsterfiles/Charmeleon/Walk (8).png",
    "res/monsterfiles/Charizard/Dead (1).png",
    "res/monsterfiles/Charizard/Idle (1).png",
    "res/monsterfiles/Charizard/Idle (2).png",
    "res/monsterfiles/Charizard/Idle (3).png",
    "res/monsterfiles/Charizard/Idle (4).png",
    "res/monsterfiles/Charizard/Idle (5).png",
    "res/monsterfiles/Charizard/Idle (6).png",
    "res/monsterfiles/Charizard/Idle (7).png",
    "res/monsterfiles/Charizard/Walk (1).png",
    "res/monsterfiles/Charizard/Walk (2).png",
    "res/monsterfiles/Charizard/Walk (3).png",
    "res/monsterfiles/Charizard/Walk (4).png",
    "res/monsterfiles/Charizard/Walk (5).png",
    "res/monsterfiles/Squirtle/Dead (1).png",
    "res/monsterfiles/Squirtle/Idle (1).png",
    "res/monsterfiles/Squirtle/Idle (2).png",
    "res/monsterfiles/Squirtle/Idle (3).png",
    "res/monsterfiles/Squirtle/Walk (1).png",
    "res/monsterfiles/Squirtle/Walk (2).png",
    "res/monsterfiles/Squirtle/Walk (3).png",
    "res/monsterfiles/Squirtle/Walk (4).png",
    "res/monsterfiles/Squirtle/Walk (5).png",
    "res/monsterfiles/Squirtle/Walk (6).png",
    "res/monsterfiles/Wartortle/Dead (1).png",
    "res/monsterfiles/Wartortle/Idle (1).png",
    "res/monsterfiles/Wartortle/Idle (2).png",
    "res/monsterfiles/Wartortle/Idle (3).png",
    "res/monsterfiles/Wartortle/Idle (4).png",
    "res/monsterfiles/Wartortle/Idle (5).png",
    "res/monsterfiles/Wartortle/Idle (6).png",
    "res/monsterfiles/Wartortle/Idle (7).png",
    "res/monsterfiles/Wartortle/Walk (1).png",
    "res/monsterfiles/Wartortle/Walk (2).png",
    "res/monsterfiles/Wartortle/Walk (3).png",
    "res/monsterfiles/Wartortle/Walk (4).png",
    "res/monsterfiles/Wartortle/Walk (5).png",
    "res/monsterfiles/Wartortle/Walk (6).png",
    "res/monsterfiles/Wartortle/Walk (7).png",
    "res/monsterfiles/Wartortle/Walk (8).png",
    "res/monsterfiles/Blastoise/Dead (1).png",
    "res/monsterfiles/Blastoise/Idle (1).png",
    "res/monsterfiles/Blastoise/Idle (2).png",
    "res/monsterfiles/Blastoise/Idle (3).png",
    "res/monsterfiles/Blastoise/Idle (4).png",
    "res/monsterfiles/Blastoise/Idle (5).png",
    "res/monsterfiles/Blastoise/Idle (6).png",
    "res/monsterfiles/Blastoise/Idle (7).png",
    "res/monsterfiles/Blastoise/Walk (1).png",
    "res/monsterfiles/Blastoise/Walk (2).png",
    "res/monsterfiles/Blastoise/Walk (3).png",
    "res/monsterfiles/Blastoise/Walk (4).png",
    "res/monsterfiles/Blastoise/Walk (5).png",
    "res/monsterfiles/Blastoise/Walk (6).png",
    "res/monsterfiles/Blastoise/Walk (7).png",
    "res/monsterfiles/Blastoise/Walk (8).png",

]

FONT_PAIRS = [
    ("res/ENCR10B.TTF", 10),
    ("res/ENCR10B.TTF", 20),
    ("res/ENCR10B.TTF", 30),
]

if __name__ == '__main__':
    gfw.run_main()
