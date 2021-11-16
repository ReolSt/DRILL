import game_framework
from pico2d import *
from ball import Ball

import game_world

class Bird:
    # Bird Run Speed
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    SPEED_KMPH = 50.0  # Km / Hour
    # 평균적인 새의 속도입니다.
    SPEED_MPM = (SPEED_KMPH * 1000.0 / 60.0)
    SPEED_MPS = (SPEED_MPM / 60.0)
    SPEED_PPS = (SPEED_MPS * PIXEL_PER_METER)

    # Bird Action Speed
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 14

    # 날갯짓 속도는 한 사이클에 0.7초가 걸립니다.

    image = None

    def __init__(self, x=100, y=100, dir=1):
        self.x, self.y = x, y

        if Bird.image is None:
            Bird.image = load_image('bird100x100x14.png')

        self.image = Bird.image

        self.dir = dir
        self.velocity = Bird.SPEED_PPS

        self.frame = 0

    def update(self):
        self.frame = (self.frame + Bird.FRAMES_PER_ACTION * Bird.ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.velocity * self.dir * game_framework.frame_time

        if self.x <= 0:
            self.dir = 1
        elif self.x >= 1600:
            self.dir = -1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(100 * int(self.frame), 0, 100, 100, 0, '', self.x, self.y, 30, 30)
        else:
            self.image.clip_composite_draw(100 * int(self.frame), 0, 100, 100, 0, 'h', self.x, self.y, 30, 30)

        #새의 크기는 참새 등의 크기로 설정하면 너무 작게 보이므로 90cm로 정했습니다.
