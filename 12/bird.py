import game_framework
from pico2d import *
from ball import Ball

import game_world

class Bird:
    # Bird Run Speed
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    SPEED_KMPH = 50.0  # Km / Hour
    # ������� ���� �ӵ��Դϴ�.
    SPEED_MPM = (SPEED_KMPH * 1000.0 / 60.0)
    SPEED_MPS = (SPEED_MPM / 60.0)
    SPEED_PPS = (SPEED_MPS * PIXEL_PER_METER)

    # Bird Action Speed
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 14

    # ������ �ӵ��� �� ����Ŭ�� 0.7�ʰ� �ɸ��ϴ�.

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

        #���� ũ��� ���� ���� ũ��� �����ϸ� �ʹ� �۰� ���̹Ƿ� 90cm�� ���߽��ϴ�.
