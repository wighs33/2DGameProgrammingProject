import gfw
from pico2d import *
import main_state
from gobj import res

canvas_width = main_state.canvas_width
canvas_height = main_state.canvas_height

center_x = canvas_width // 2
center_y = canvas_height // 2

def enter():
    global back, bg, fg, index, file
    back = gfw.image.load(res('loading.jpg'))
    bg = gfw.image.load(res('progress_bg.png'))
    fg = gfw.image.load(res('progress_fg.png'))
    index = 0

    global font, display
    font = gfw.font.load(res('ENCR10B.TTF'), 30)
    display = ''

    global frame_interval
    frame_interval = gfw.frame_interval
    gfw.frame_interval = 0

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
        gfw.change(main_state)
        return
    index += 1

def draw():
    back.draw(center_x, center_y)
    image_count = len(IMAGE_FILES)
    font_count = len(FONT_PAIRS)
    progress = index / (image_count + font_count)
    draw_progress(center_x, 300, 680, progress)

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
    "res/kpu_1280x960.png",
    "res/animation_sheet.png",
    "res/monsterfiles/female/Attack (1).png",
    "res/monsterfiles/female/Attack (2).png",
    "res/monsterfiles/female/Attack (3).png",
    "res/monsterfiles/female/Attack (4).png",
    "res/monsterfiles/female/Attack (5).png",
    "res/monsterfiles/female/Attack (6).png",
    "res/monsterfiles/female/Attack (7).png",
    "res/monsterfiles/female/Attack (8).png",
    "res/monsterfiles/female/Attack (9).png",
    "res/monsterfiles/female/Attack (10).png",
    "res/monsterfiles/female/Dead (1).png",
    "res/monsterfiles/female/Dead (2).png",
    "res/monsterfiles/female/Dead (3).png",
    "res/monsterfiles/female/Dead (4).png",
    "res/monsterfiles/female/Dead (5).png",
    "res/monsterfiles/female/Dead (6).png",
    "res/monsterfiles/female/Dead (7).png",
    "res/monsterfiles/female/Dead (8).png",
    "res/monsterfiles/female/Dead (9).png",
    "res/monsterfiles/female/Dead (10).png",
    "res/monsterfiles/female/Dead (11).png",
    "res/monsterfiles/female/Dead (12).png",
    "res/monsterfiles/female/Idle (1).png",
    "res/monsterfiles/female/Idle (2).png",
    "res/monsterfiles/female/Idle (3).png",
    "res/monsterfiles/female/Idle (4).png",
    "res/monsterfiles/female/Idle (5).png",
    "res/monsterfiles/female/Idle (6).png",
    "res/monsterfiles/female/Idle (7).png",
    "res/monsterfiles/female/Idle (8).png",
    "res/monsterfiles/female/Idle (9).png",
    "res/monsterfiles/female/Idle (10).png",
    "res/monsterfiles/female/Idle (11).png",
    "res/monsterfiles/female/Idle (12).png",
    "res/monsterfiles/female/Idle (13).png",
    "res/monsterfiles/female/Idle (14).png",
    "res/monsterfiles/female/Idle (15).png",
    "res/monsterfiles/female/Walk (1).png",
    "res/monsterfiles/female/Walk (2).png",
    "res/monsterfiles/female/Walk (3).png",
    "res/monsterfiles/female/Walk (4).png",
    "res/monsterfiles/female/Walk (5).png",
    "res/monsterfiles/female/Walk (6).png",
    "res/monsterfiles/female/Walk (7).png",
    "res/monsterfiles/female/Walk (8).png",
    "res/monsterfiles/female/Walk (9).png",
    "res/monsterfiles/female/Walk (10).png",
    "res/monsterfiles/male/Attack (1).png",
    "res/monsterfiles/male/Attack (2).png",
    "res/monsterfiles/male/Attack (3).png",
    "res/monsterfiles/male/Attack (4).png",
    "res/monsterfiles/male/Attack (5).png",
    "res/monsterfiles/male/Attack (6).png",
    "res/monsterfiles/male/Attack (7).png",
    "res/monsterfiles/male/Attack (8).png",
    "res/monsterfiles/male/Dead (1).png",
    "res/monsterfiles/male/Dead (2).png",
    "res/monsterfiles/male/Dead (3).png",
    "res/monsterfiles/male/Dead (4).png",
    "res/monsterfiles/male/Dead (5).png",
    "res/monsterfiles/male/Dead (6).png",
    "res/monsterfiles/male/Dead (7).png",
    "res/monsterfiles/male/Dead (8).png",
    "res/monsterfiles/male/Dead (9).png",
    "res/monsterfiles/male/Dead (10).png",
    "res/monsterfiles/male/Dead (11).png",
    "res/monsterfiles/male/Dead (12).png",
    "res/monsterfiles/male/Idle (1).png",
    "res/monsterfiles/male/Idle (2).png",
    "res/monsterfiles/male/Idle (3).png",
    "res/monsterfiles/male/Idle (4).png",
    "res/monsterfiles/male/Idle (5).png",
    "res/monsterfiles/male/Idle (6).png",
    "res/monsterfiles/male/Idle (7).png",
    "res/monsterfiles/male/Idle (8).png",
    "res/monsterfiles/male/Idle (9).png",
    "res/monsterfiles/male/Idle (10).png",
    "res/monsterfiles/male/Idle (11).png",
    "res/monsterfiles/male/Idle (12).png",
    "res/monsterfiles/male/Idle (13).png",
    "res/monsterfiles/male/Idle (14).png",
    "res/monsterfiles/male/Idle (15).png",
    "res/monsterfiles/male/Walk (1).png",
    "res/monsterfiles/male/Walk (2).png",
    "res/monsterfiles/male/Walk (3).png",
    "res/monsterfiles/male/Walk (4).png",
    "res/monsterfiles/male/Walk (5).png",
    "res/monsterfiles/male/Walk (6).png",
    "res/monsterfiles/male/Walk (7).png",
    "res/monsterfiles/male/Walk (8).png",
    "res/monsterfiles/male/Walk (9).png",
    "res/monsterfiles/male/Walk (10).png",
]

FONT_PAIRS = [
    ("res/ENCR10B.TTF", 10),
    ("res/ENCR10B.TTF", 20),
    ("res/ENCR10B.TTF", 30),
]

if __name__ == '__main__':
    gfw.run_main()
