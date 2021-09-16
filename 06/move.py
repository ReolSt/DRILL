from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y, rad = 400, 90, math.pi * 3 / 2
dx, dy, dr = 3, 3, 0.015
r = 250

def render():
    global x, y
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

while True:
    while x < 750:
        render()
        x += dx
    while y < 550:
        render()
        y += dy
    while x > 50:
        render()
        x -= dx
    while y > 90:
        render()
        y -= dy

    while x < 400:
        render()
        x += dx
    while rad > -math.pi / 2:
        render()
        x = 400 + math.cos(rad) * r
        y = 90 + r + math.sin(rad) * r
        rad -= dr
    x, y, rad = 400, 90, math.pi * 3 / 2

close_canvas()
