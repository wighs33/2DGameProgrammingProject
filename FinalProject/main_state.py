import os.path
import gfw
from pico2d import *
from unit import Unit
from unit import Unit
from monster import Monster
import gobj
import life_gauge
import gameclear

canvas_width = 1000
canvas_height = 900
isclear = False
is_lose=False
max_monster_number = 30

SAVE_FILENAME = 'monsters.pickle'

def enter():
    gfw.world.init(['bg', 'monster', 'unit', 'unit', "gameclear"])
    Monster.load_all_images()
    Unit.load_all_images()
    life_gauge.load()
    gameclear.load()

    global selectedUnit

    if load():
        unit = gfw.world.object(gfw.layer.unit, 0)
    else:
        unit = Unit(1)
        selectedUnit = unit
        gfw.world.add(gfw.layer.unit, unit)
        gfw.world.add(gfw.layer.unit, Unit(1))
        gfw.world.add(gfw.layer.unit, Unit(1))
        gfw.world.add(gfw.layer.unit, Unit(1))

        bg = gobj.ImageObject('background.jpg', (canvas_width // 2, canvas_height // 2))
        gfw.world.add(gfw.layer.bg, bg)

    global magic_circle
    magic_circle = gfw.image.load(gobj.RES_DIR + '/magic.png')

    global font, font2
    font = gfw.font.load(gobj.RES_DIR + '/Sweet_story.otf', 50)
    font2 = gfw.font.load(gobj.RES_DIR + '/ConsolaMalgun.ttf', 20)

    global monster_time
    monster_time = 1
    global monster_level
    monster_level = 1
    global monster_level_up_time
    monster_level_up_time = 50
    global unit_time
    unit_time = 50


def load():
    if not os.path.isfile(SAVE_FILENAME):
        return False

    gfw.world.load(SAVE_FILENAME)
    print('Loaded from:', SAVE_FILENAME)
    return True

def check_monster(mon):
    for u2 in gfw.gfw.world.objects_at(gfw.layer.unit):
        if gobj.attack_box(u2, mon):
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
    global isclear
    global is_lose
    monster_time -= gfw.delta_time
    monster_level_up_time -= gfw.delta_time
    if monster_time <= 0:
        if monster_level_up_time <= 0:
            monster_level += 1
            if monster_level == 10:
                isclear = True
                end_game()
            monster_level_up_time = 50
        if not is_lose: gfw.world.add(gfw.layer.monster, Monster(monster_level))
        monster_time = 5

    if gfw.world.count_at(gfw.layer.monster) >= max_monster_number:
        isclear = False
        is_lose=True
        end_game()
    global unit_time
    global unit
    unit_time -= gfw.delta_time
    if unit_time <= 0:
        if not is_lose: gfw.world.add(gfw.layer.unit, Unit())
        unit_time = 50

    for mon in gfw.world.objects_at(gfw.layer.monster):
        check_monster(mon)
    ok=False
    for unit1 in gfw.world.objects_at(gfw.layer.unit):
        for unit2 in gfw.world.objects_at(gfw.layer.unit):
            if gobj.can_combination(unit1, unit2) and unit1 != unit2:
                unit1.remove()
                unit2.remove()
                ok = True

    if ok: gfw.world.add(gfw.layer.unit, Unit(2))

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    gobj.draw_attack_box()
    magic_circle.draw(gobj.magic_circle_pos[0], gobj.magic_circle_pos[1])
    draw_rectangle(*gobj.magic_circle_bb())
    font.draw(300, canvas_height - 60, 'Stage %d' % monster_level,(255,50,255))
    font2.draw(550, canvas_height - 60, 'Number of Monsters: %d/%d' % (gfw.world.count_at(gfw.layer.monster), max_monster_number))
    if isclear and end_game(): gameclear.button_image.draw_to_origin(get_canvas_width()//2 - gameclear.button_image.w//2, 80)
    
def handle_event(e):
    global selectedUnit
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    if e.type == SDL_MOUSEBUTTONDOWN:
        if gameclear.is_click_continue(e): gfw.world.clear_at(gfw.layer.gameclear)
        selectTmp=gobj.select_unit(e)
        if hasattr(selectTmp, 'handle_event'):
            selectedUnit = selectTmp
    selectedUnit.handle_event(e)

    # if e.type == SDL_KEYDOWN and e.key == SDLK_s:
    #     gfw.world.save(SAVE_FILENAME)
    #     print('Saved to:', SAVE_FILENAME)

def end_game():
    global isclear
    if isclear: 
        gameclear.add()
    gfw.world.add(gfw.layer.gameclear, gameclear)
    return True

def exit():
    pass

if __name__ == '__main__':
    print("This file is not supposed to be executed directly.")
