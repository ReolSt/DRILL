from pico2d import *

import random


open_canvas()

boySprite = load_image('run_animation.png')
grassSprite = load_image('grass.png')
smallBallSprite = load_image('ball21x21.png')
bigBallSprite = load_image('ball41x41.png')

class Grass:
    def __init__(self):
        self.x = 400
        self.y = 30

        self.sprite = grassSprite

    def draw(self):
        self.sprite.draw(self.x, self.y)

class Ball:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 599

        self.speed = (random.random() + 1.0) * 2

    def draw(self):
        if hasattr(self, "sprite"):
            self.sprite.draw(self.x, self.y)

    def update(self):
        self.y -= self.speed

        if hasattr(self, "sprite"):
            if self.y - self.sprite.h / 2 <= 55:
                self.speed = 0

class SmallBall(Ball):
    def __init__(self):
        super().__init__()

        self.sprite = smallBallSprite

class BigBall(Ball):
    def __init__(self):
        super().__init__()

        self.sprite = bigBallSprite


running = True
x = 800 // 2
frame = 0

grass = Grass()
balls = []

for i in range(20):
    r = random.randint(0, 2)
    ball = SmallBall() if r == 0 else BigBall()
    balls.append(ball)

while running:
    clear_canvas()

    grass.draw()

    for i in range(20):
        balls[i].update()
        balls[i].draw()

    update_canvas()

    frame = (frame + 1) % 8

    delay(0.02)

close_canvas()

