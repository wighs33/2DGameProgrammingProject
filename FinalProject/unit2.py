import random
from pico2d import *
import gfw
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Unit2:
    ACTIONS = ['Attack', 'Idle', 'Walk']
    CHASE_DISTANCE_SQ = 250 ** 2
    IDLE_INTERVAL = 2.0
    images = {}
    FPS = 10
    # FCOUNT = 10
    def __init__(self):
        if len(Unit2.images) == 0:
            Unit2.load_all_images()

        self.pos = get_canvas_width()//2,get_canvas_height()//2
        self.delta = 0, 0
        # self.find_nearest_pos()
        self.char = random.choice(['Ace', 'Akainu', 'Aokiji', 'Bartholomew Kuma', 'Blackbeard', 'Boa Hancock', 'Buggy', 'Chopper', 'Crocodile', 'Dracule Mihawk', 
            'Emporio Ivankov', 'Jinbei', 'Kizaru', 'MonkeyDLuffy'])
        self.images = Unit2.load_images(self.char)
        self.action = 'Idle'
        self.speed = 200
        self.fidx = 0
        self.time = 0
        self.target = None
        if gfw.world.count_at(gfw.layer.unit) > 0:
            self.unit = gfw.world.object(gfw.layer.unit, 0)
        self.patrol_order = -1
        self.build_behavior_tree()

        self.power_by_char()

    def power_by_char(self):
        self.power = \
            17 if self.char == 'Ace' else \
            20 if self.char == 'Akainu' else \
            20 if self.char == 'Aokiji' else \
            18 if self.char == 'Bartholomew Kuma' else \
            21 if self.char == 'Blackbeard' else \
            15 if self.char == 'Boa Hancock' else \
            14 if self.char == 'Buggy' else \
            13 if self.char == 'Chopper' else \
            16 if self.char == 'Crocodile' else \
            20 if self.char == 'Dracule Mihawk' else \
            17 if self.char == 'Emporio Ivankov' else \
            18 if self.char == 'Jinbei' else \
            19 if self.char == 'Kizaru' else \
            16 if self.char == 'MonkeyDLuffy' else 10
    def set_target(self, target):
        x,y = self.pos
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance
        # print(x,y, tx,ty, dx,dy, '/',distance, dx/distance, dy/distance, 'target=', self.target, ' delta=', self.delta)

    # def find_unit(self):
    #     dist_sq = gobj.distance_sq(self.unit.pos, self.pos)
    #     if dist_sq < Unit2.CHASE_DISTANCE_SQ:
    #         if self.patrol_order >= 0:
    #             self.patrol_order = -1
    #             self.action = 'Attack'
    #         return BehaviorTree.SUCCESS
    #     else:
    #         if self.action == 'Attack':
    #             self.action = 'Idle'
    #             self.time = 0
    #         else:
    #             self.action = 'Walk'
    #         return BehaviorTree.FAIL

    # def move_to_unit(self):
    #     self.set_target(self.unit.pos)
    #     self.update_position()

    #     collides = gobj.collides_box(self, self.unit)
    #     if collides:
    #         self.action = 'Dead'
    #         self.time = 0
    #     return BehaviorTree.SUCCESS

    # def follow_patrol_positions(self):
    #     if self.patrol_order < 0:
    #         self.find_nearest_pos()
    #     done = self.update_position()
    #     if done:
    #         self.set_patrol_target()

    def do_idle(self):
        if self.action != 'Idle':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Unit2.FPS)
        if self.delta[0] != 0 or self.delta[1] != 0:
            self.action = 'Walk'
            return BehaviorTree.FAIL
        for mon in gfw.world.objects_at(gfw.layer.monster):
            if gobj.attack_box(self, mon):
                self.action = 'Attack'
                self.time = 0
                return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_walk(self):
        if self.action != 'Walk':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Unit2.FPS)
        if self.delta[0] == 0 and self.delta[1] == 0:
            self.action = 'Idle'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_attack(self):
        if self.action != 'Attack':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Unit2.FPS)
        if self.fidx >= len(self.images['Attack']):
            self.action = 'Idle'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS


    @staticmethod
    def load_all_images():
        Unit2.load_images('Ace')
        Unit2.load_images('Akainu')
        # Unit2.font = gfw.font.load(gobj.RES_DIR + '/ENCR10B.TTF', 20)

    @staticmethod
    def load_images(char):
        if char in Unit2.images:
            return Unit2.images[char]

        images = {}
        count = 0
        file_fmt = '%s/unitfiles/%s/%s (%d).png'
        for action in Unit2.ACTIONS:
            action_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, action, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Unit2.images[char] = images
        #print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.bt.run()
        self.update_position()

    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Unit2.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        # print(self.pos, self.delta, self.target, x, y, dx, dy)

        done = False
        done = False
        if self.target is not None:
            tx, ty = self.target
            if dx > 0 and x >= tx or dx < 0 and x <= tx:
                x = tx
                done = True
            if dy > 0 and y >= ty or y < 0 and y <= ty:
                y = ty
                done = True
            self.pos = x,y

        if done:
            self.target = None
            self.delta = 0, 0

        

        return done

    def handle_event(self, e):
        pair = (e.type, e.key)
        # if pair in Unit.KEY_MAP:
        #     if self.target is not None:
        #         self.target = None
        #         self.delta = 0, 0
        #     pdx = self.delta[0]
        #     self.delta = gobj.point_add(self.delta, Unit.KEY_MAP[pair])
        #     dx = self.delta[0]
        #     self.action = \
        #         0 if dx < 0 else \
        #         1 if dx > 0 else \
        #         2 if pdx < 0 else 3
        #     print(dx, pdx, self.action)

        if e.type == SDL_MOUSEBUTTONDOWN:
            self.set_target((e.x, get_canvas_height() - e.y - 1))
            # print("(",e.x,",", get_canvas_height() - e.y - 1,")")

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.composite_draw(0, flip, *self.pos, image.w, image.h)
        # x,y = self.pos
        # Unit2.font.draw(x-40, y+50, self.action + str(round(self.time * 100) / 100))

    def get_bb(self):
        x,y = self.pos
        return x - 30, y - 40, x + 30, y + 40

    def get_attack_range(self):
        x,y = self.pos
        return x - 80, y - 80, x + 80, y + 80


    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['images']
        # del dict['unit']
        return dict

    def __setstate__(self, dict):
        # self.__init__()
        self.__dict__.update(dict)
        self.images = Unit2.load_images(self.char)

    def build_behavior_tree(self):
        # node_gnp = LeafNode("Get Next Position", self.set_patrol_target)
        # node_mtt = LeafNode("Move to Target", self.update_position)
        # patrol_node = SequenceNode("Patrol")
        # patrol_node.add_children(node_gnp, node_mtt)
        # self.bt = BehaviorTree(patrol_node)

        self.bt = BehaviorTree.build({
            "name": "PatrolChase",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Idle",
                    "function": self.do_idle,
                },
                {
                    "class": LeafNode,
                    "name": "Walk",
                    "function": self.do_walk,
                },
                {
                    "class": LeafNode,
                    "name": "Attack",
                    "function": self.do_attack,
                },
            ],
        })
