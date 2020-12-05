import random
from pico2d import *
import gfw

RES_DIR = 'res'

def res(file):
    return RES_DIR + '/' + file

def rand(val):
    return val * random.uniform(0.9, 1.1)

def point_add(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return x1+x2, y1+y2

def move_obj(obj):
    obj.pos = point_add(obj.pos, obj.delta)

def collides_box(a, b):
    (la, ba, ra, ta) = a.get_bb()
    (lb, bb, rb, tb) = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ba > tb: return False
    if ta < bb: return False

    return True

def attack_box(attacker, mon):
    (la, ba, ra, ta) = attacker.get_attack_range()
    (lb, bb, rb, tb) = mon.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ba > tb: return False
    if ta < bb: return False

    return True

def select_unit(e):
    if e.type == SDL_MOUSEBUTTONDOWN:
        for obj in gfw.world.all_objects():
            if hasattr(obj, 'get_bb'):
                if hasattr(obj, 'handle_event'):
                    (la, ba, ra, ta) = obj.get_bb()

                    if la < e.x and ra > e.x and ba < get_canvas_height() - e.y - 1 and ta > get_canvas_height() - e.y - 1:
                        return obj

def distance_sq(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return (x1-x2)**2 + (y1-y2)**2

def distance(point1, point2):
    math.sqrt(distance_sq(point1, point2))
    
def draw_collision_box():
    for obj in gfw.world.all_objects():
        if hasattr(obj, 'get_bb'):
            draw_rectangle(*obj.get_bb())

def draw_attack_box():
    for obj in gfw.world.objects_at(gfw.layer.unit2):
        draw_rectangle(*obj.get_attack_range())

class ImageObject:
    def __init__(self, imageName, pos):
        self.imageName = imageName
        self.image = gfw.image.load(RES_DIR + '/' + imageName)
        self.pos = pos
    def draw(self):
        self.image.draw(*self.pos)
    def update(self):
        pass
    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict
    def __setstate__(self, dict):
        self.__dict__.update(dict)
        self.image = gfw.image.load(RES_DIR + '/' + self.imageName)

if __name__ == "__main__":
    print("This file is not supposed to be executed directly.")
