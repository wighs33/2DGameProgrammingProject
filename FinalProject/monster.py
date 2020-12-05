import random
from pico2d import *
import gfw
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import life_gauge

class Monster:
    PAT_POSITIONS = [
        (278, 244), (601, 158), (926, 236), (1041, 528), 
        (916, 844), (606, 882), (286, 825), (153, 542)
    ]
    ACTIONS = ['Dead', 'Idle', 'Walk']
    CHASE_DISTANCE_SQ = 250 ** 2
    IDLE_INTERVAL = 2.0
    images = {}
    FPS = 10
    # FCOUNT = 10
    def __init__(self, level):
        if len(Monster.images) == 0:
            Monster.load_all_images()

        self.pos = 920,60
        self.delta = 0.1, 0.1
        # self.find_nearest_pos()
        self.level = level
        self.max_life = level * 100
        self.life = self.max_life
        self.strong_monster_by_level()
        self.images = Monster.load_images(self.char)
        self.action = 'Idle'
        self.speed = 100
        self.fidx = 0
        self.time = 0
        if gfw.world.count_at(gfw.layer.unit) > 0:
            self.unit = gfw.world.object(gfw.layer.unit, 0)
        self.patrol_order = -1
        self.build_behavior_tree()

    def strong_monster_by_level(self):
        self.char = \
            'Bulbasaur' if self.level == 1 else \
            'Charmander' if self.level == 2 else \
            'Squirtle' if self.level == 3 else \
            'Ivysaur' if self.level == 4 else \
            'Charmeleon' if self.level == 5 else \
            'Wartortle' if self.level == 6 else \
            'Venusaur' if self.level == 7 else \
            'Charizard' if self.level == 8 else 'Blastoise'

    def find_nearest_pos(self):
        x, y = self.pos
        nearest_dsq = 1000000000
        index = 0
        nearest_index = 0
        for (px, py) in Monster.PAT_POSITIONS:
            dsq = (x-px)**2 + (y-py)**2
            #print(':', index, (x,y), '-', (px, py), dsq)
            if nearest_dsq > dsq:
                nearest_dsq = dsq
                nearest_index = index
                #print('nearest:', index)
            index += 1
        self.patrol_order = nearest_index
        self.set_patrol_target()

    def set_patrol_target(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
            return BehaviorTree.SUCCESS
        self.set_target(Monster.PAT_POSITIONS[self.patrol_order])
        # print('pos=', self.pos, "patrol order = ", self.patrol_order, " target =", self.target)
        self.patrol_order = (self.patrol_order + 1) % len(Monster.PAT_POSITIONS)
        return BehaviorTree.SUCCESS

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
    #     if dist_sq < Monster.CHASE_DISTANCE_SQ:
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

    def follow_patrol_positions(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
        done = self.update_position()
        if done:
            self.set_patrol_target()
        if self.life <= 0:
            self.action = 'Dead'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_idle(self):
        if self.action != 'Idle':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster.FPS)
        if self.time >= Monster.IDLE_INTERVAL:
            self.action = 'Walk'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_dead(self):
        if self.action != 'Dead':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster.FPS)
        if self.fidx >= len(self.images['Dead']):
            self.remove()

        return BehaviorTree.SUCCESS

    def decrease_life(self, amount):
        self.life -= amount

    @staticmethod
    def load_all_images():
        Monster.load_images('male')
        Monster.load_images('female')
        # Monster.font = gfw.font.load(gobj.RES_DIR + '/ENCR10B.TTF', 20)

    @staticmethod
    def load_images(char):
        if char in Monster.images:
            return Monster.images[char]

        images = {}
        count = 0
        file_fmt = '%s/monsterfiles/%s/%s (%d).png'
        for action in Monster.ACTIONS:
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
        Monster.images[char] = images
        #print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.bt.run()

    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Monster.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        # print(self.pos, self.delta, self.target, x, y, dx, dy)

        done = False
        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or y < 0 and y <= ty:
            y = ty
            done = True

        self.pos = x,y

        return done

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] > 0 else ''
        image.composite_draw(0, flip, *self.pos, image.w, image.h)

        gy = self.pos[1] + image.h//2
        rate = self.life / self.max_life
        life_gauge.draw(self.pos[0], gy, 30, rate)
        # x,y = self.pos
        # Monster.font.draw(x-40, y+50, self.action + str(round(self.time * 100) / 100))

    def get_bb(self):
        x, y = self.pos
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        return x - image.w//2, y - image.h//2, x + image.w//2, y + image.h//2

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['images']
        # del dict['unit']
        return dict

    def __setstate__(self, dict):
        # self.__init__()
        self.__dict__.update(dict)
        self.images = Monster.load_images(self.char)

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
                    "name": "Dead",
                    "function": self.do_dead,
                },
                #{
                #    "name": "Chase",
                #    "class": SequenceNode,
                #    "children": [
                        #{
                        #    "class": LeafNode,
                        #    "name": "Find Unit",
                        #    "function": self.find_unit,
                        #},
                        #{
                        #    "class": LeafNode,
                        #    "name": "Move to Unit",
                        #    "function": self.move_to_unit,
                        #},
                #    ],
                #},
                {
                    "class": LeafNode,
                    "name": "Follow Patrol positions",
                    "function": self.follow_patrol_positions,
                },
            ],
        })
