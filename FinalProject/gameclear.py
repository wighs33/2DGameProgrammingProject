import pickle
from pico2d import *
import time
import gfw
import gobj

FILENAME = 'data.pickle'
gameclears = []

class Entry:
    def __init__(self):
        self.time = time.time()

def load():
    global font, image, button_image
    font = gfw.font.load(gobj.res('ConsolaMalgun.ttf'), 20)
    image = gfw.image.load(gobj.res('game_over.png'))
    button_image = gfw.image.load(gobj.res('continue.png'))

    try:
        f = open(FILENAME, "rb")
        gameclears = pickle.load(f)
        f.close()
    except:
        print("No clear file")

def save():
    f = open(FILENAME, "wb")
    pickle.dump(gameclears, f)
    f.close()

def add():
    gameclears.append(Entry())

def draw():
    global font, image
    image.draw_to_origin(get_canvas_width()//2-image.w//2, get_canvas_height()//2-image.h//2)
    y = 360
    for c in gameclears:
        font.draw(get_canvas_width()//2-image.w//2 + 30, get_canvas_height()//2-image.h//2 + y, "clear!", (255, 255, 128))
        font.draw(get_canvas_width()//2-image.w//2 + 220, get_canvas_height()//2-image.h//2 + y, time.asctime(time.localtime(c.time)), (223, 255, 223))
        y -= 30

def is_click_continue(e):
    global button_image
    if e.type == SDL_MOUSEBUTTONDOWN:
        (la, ba, ra, ta) = get_canvas_width()//2-button_image.w//2, 80, get_canvas_width()//2 + button_image.w//2, 80 + button_image.h

        if la < e.x and ra > e.x and ba < get_canvas_height() - e.y - 1 and ta > get_canvas_height() - e.y - 1:
            return True
    return False

def update():
    pass
