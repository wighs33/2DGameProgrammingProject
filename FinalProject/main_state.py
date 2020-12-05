import os.path
import gfw
from pico2d import *
from unit import Unit
from unit2 import Unit2
from monster import Monster
import gobj
import life_gauge

canvas_width = 1200
canvas_height = 1020

SAVE_FILENAME = 'monsters.pickle'

def enter():
    gfw.world.init(['bg', 'monster', 'unit', 'unit2'])
    Monster.load_all_images()
    Unit2.load_all_images()
    life_gauge.load()

    global selectedUnit

    if load():
        unit = gfw.world.object(gfw.layer.unit2, 0)
    else:
        unit = Unit2()
        selectedUnit = unit
        gfw.world.add(gfw.layer.unit2, unit)
        gfw.world.add(gfw.layer.unit2, Unit2())
        gfw.world.add(gfw.layer.unit2, Unit2())

        bg = gobj.ImageObject('background.jpg', (canvas_width // 2, canvas_height // 2))
        gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

    global monster_time
    monster_time = 1
    global monster_level
    monster_level = 1
    global monster_level_up_time
    monster_level_up_time = 49
    global unit_time
    unit_time = 50


def load():
    if not os.path.isfile(SAVE_FILENAME):
        return False

    gfw.world.load(SAVE_FILENAME)
    print('Loaded from:', SAVE_FILENAME)
    return True

def check_monster(mon):
    for u2 in gfw.gfw.world.objects_at(gfw.layer.unit2):
        if gobj.collides_box(u2, mon):
            if u2.action == 'Attack':
                # print('Collision', e, b)
                dead = mon.decrease_life(u2.power)
                if dead:
                    mon.remove()
                return

def update():
    gfw.world.update()

    global monster_time
    global monster_level_up_time
    global monster_level
    monster_time -= gfw.delta_time
    monster_level_up_time -= gfw.delta_time
    if monster_time <= 0:
        gfw.world.add(gfw.layer.monster, Monster(monster_level))
        if monster_level_up_time <= 0:
            monster_level += 1
            monster_level_up_time = 49
        monster_time = 5

    global unit_time
    global unit2
    unit_time -= gfw.delta_time
    if unit_time <= 0:
        gfw.world.add(gfw.layer.unit2, Unit2())
        unit_time = 50

    for mon in gfw.world.objects_at(gfw.layer.monster):
        check_monster(mon)

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    gobj.draw_attack_box()
    font.draw(canvas_width//2-100, canvas_height - 60, 'Stage: %d' % monster_level)
    
def handle_event(e):
    global selectedUnit
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    if e.type == SDL_MOUSEBUTTONDOWN:
        # unit2.handle_event(e)
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
