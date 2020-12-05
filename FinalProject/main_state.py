import os.path
import gfw
from pico2d import *
from unit import Unit
from monster import Monster
import gobj

canvas_width = 1200
canvas_height = 1020

SAVE_FILENAME = 'monsters.pickle'

def enter():
    gfw.world.init(['bg', 'monster', 'unit'])
    Monster.load_all_images()

    global selectedUnit

    if load():
        unit = gfw.world.object(gfw.layer.unit, 0)
    else:
        unit = Unit(gfw.image.load(gobj.RES_DIR + '/Ace_run.png'), (get_canvas_width() // 2 + 100, get_canvas_height() // 2), [0, 78, 144, 207, 256, 321, 389, 452, 513])
        unit2 = Unit(gfw.image.load(gobj.RES_DIR + '/MonkeyDLuffy_run.png'), (get_canvas_width() // 2, get_canvas_height() // 2), [0, 45, 100, 165, 218, 261, 317, 381, 441])
        unit3 = Unit(gfw.image.load(gobj.RES_DIR + '/Akainu_run.png'), (get_canvas_width() // 2 -100, get_canvas_height() // 2), [0, 51, 106, 170, 232, 285, 338, 396, 445])
        unit4 = Unit(gfw.image.load(gobj.RES_DIR + '/Aokiji_run.png'), (get_canvas_width() // 2, get_canvas_height() // 2-100), [0, 54, 116, 193, 261, 319, 370, 420, 478])
        selectedUnit = unit
        gfw.world.add(gfw.layer.unit, unit)
        gfw.world.add(gfw.layer.unit, unit2)
        gfw.world.add(gfw.layer.unit, unit3)
        gfw.world.add(gfw.layer.unit, unit4)

        bg = gobj.ImageObject('background.jpg', (canvas_width // 2, canvas_height // 2))
        gfw.world.add(gfw.layer.bg, bg)

    global monster_time
    monster_time = 1

def load():
    if not os.path.isfile(SAVE_FILENAME):
        return False

    gfw.world.load(SAVE_FILENAME)
    print('Loaded from:', SAVE_FILENAME)
    return True

def update():
    gfw.world.update()

    global monster_time
    monster_time -= gfw.delta_time
    if monster_time <= 0:
        gfw.world.add(gfw.layer.monster, Monster())
        monster_time = 5

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    
def handle_event(e):
    global selectedUnit
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    if e.type == SDL_MOUSEBUTTONDOWN:
        selectTmp=gobj.select_unit(e)
        if hasattr(selectTmp, 'handle_event'):
            selectedUnit = selectTmp
    selectedUnit.handle_event(e)

    # if e.type == SDL_KEYDOWN and e.key == SDLK_s:
    #     gfw.world.save(SAVE_FILENAME)
    #     print('Saved to:', SAVE_FILENAME)

def exit():
    pass

if __name__ == '__main__':
    print("This file is not supposed to be executed directly.")
