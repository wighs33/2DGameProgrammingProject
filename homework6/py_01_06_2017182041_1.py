from pico2d import* 
import helper

def handle_events():
    global running
    global move
    global x, y
    global ex, ey
    global speed
    global done
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move=True
            ex=event.x
            ey=800 - event.y
            destList.append((ex,ey))
            speed+=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(800, 800)
kpu_ground = load_image('grass.png')
character = load_image('run_animation.png')

running = True
move = False
x, y = 800 // 2, 90
destList = [(800 // 2, 90)]
destListCount = 1
frame = 0
speed = 0
done = 0

while running:
    clear_canvas()
    kpu_ground.draw(800//2, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    if move:
        x, y = helper.move_toward((x,y), helper.delta((x,y), destList[destListCount], speed), destList[destListCount])[0]
        done = helper.move_toward((x,y), helper.delta((x,y), destList[destListCount], speed), destList[destListCount])[1]
    if done:
        if destListCount==len(destList)-1:
            move=False
        speed=1
        destListCount+=1
        done=0
    handle_events()