import random
import gfw
from pico2d import *
import main_state
import gobj

canvas_width = main_state.canvas_width
canvas_height = main_state.canvas_height

center_x = canvas_width // 2
center_y = canvas_height // 2

memo_on=False

def enter():
    global image, font, font2, w, h, start_button, manual_button, memo
    image = gfw.image.load(gobj.RES_DIR + '/title.jpg')
    start_button=gfw.image.load(gobj.RES_DIR + '/gamestart.jpg')
    manual_button=gfw.image.load(gobj.RES_DIR + '/manual.jpg')
    memo = gfw.image.load(gobj.RES_DIR + '/memo.png')
    font = gfw.font.load(gobj.RES_DIR + '/BRAZIE.ttf', 100)
    font2 = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 22)

    global music_bg
    music_bg = load_music('res/Track 26.mp3')
    music_bg.set_volume(10)
    music_bg.repeat_play()

def update():
    pass

def draw():
    image.draw(center_x, center_y)
    font.draw(10, get_canvas_height() - 100, 'CREATURE DEFENSE', (150, 100, 200))
    start_button.draw(850, 500)
    manual_button.draw(850, 450)
    if memo_on: 
        memo.draw(center_x, center_y)
        font2.draw(250, 830, '< How To Play >', (10, 10, 200))
        font2.draw(250, 780, 'Kill monsters by moving units with the mouse', (10, 10, 10))
        font2.draw(250, 730, 'stage 9 -> WIN', (10, 10, 10))
        font2.draw(250, 700, 'the number of monsters exceeds 30 -> LOSE', (10, 10, 10))
        font2.draw(250, 600, 'To combine, move two units to the magic circle', (10, 10, 10))
        font2.draw(250, 400, 'Press any key', (10, 10, 10))

def handle_event(e):
    global memo_on
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        memo_on = False
        if e.key == SDLK_ESCAPE:
            gfw.quit()
        if e.key == SDLK_SPACE:
            gfw.push(main_state)

    if e.type == SDL_MOUSEBUTTONDOWN:
        if 850-start_button.w//2 < e.x and \
            850+start_button.w//2 > e.x and \
            500-start_button.h//2 < get_canvas_height() - e.y - 1 and \
            500+start_button.h//2 > get_canvas_height() - e.y - 1 and not memo_on:
            gfw.push(main_state)
        elif 850-manual_button.w//2 < e.x and \
            850+manual_button.w//2 > e.x and \
            450-manual_button.h//2 < get_canvas_height() - e.y - 1 and \
            450+manual_button.h//2 > get_canvas_height() - e.y - 1 and not memo_on:
            memo_on=True


def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    print("This file is not supposed to be executed directly.")
