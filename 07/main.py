from pico2d import *

import random


open_canvas()
ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x = 800 // 2
frame = 0

def randPosition():
    return [random.randint(0, 800), random.randint(0, 600)]

def getVelocity(x, y, targetX, targetY, multiplier):
    dx = targetX - x
    dy = targetY - y

    n = (dx ** 2 + dy ** 2) ** 0.5

    return [(dx / n) * multiplier, dy / n * multiplier]

handPosition = randPosition()
characterPosition = [100, 100]
characterVelocity = getVelocity(characterPosition[0], characterPosition[1],
                                 handPosition[0], handPosition[1], 10)
characterFlipString = ""
if characterVelocity[0] < 0:
   characterFlipString = "h"

def AABB(a, b):
    if a["L"] > b["R"] or a["R"] < b["L"]:
        return False
    if a["B"] > b["T"] or a["T"] < b["B"]:
        return False

    return True

while running:
    clear_canvas()
    ground.draw(400, 300)
    hand.draw(handPosition[0], handPosition[1])
    character.clip_composite_draw(frame * 100, 100 * 1, 100, 100,
                                  0, characterFlipString,
                        characterPosition[0], characterPosition[1], 100, 100)

    handAABB = {}
    handAABB["L"] = handPosition[0] - hand.w / 2
    handAABB["R"] = handPosition[0] + hand.w / 2
    handAABB["B"] = handPosition[1] - hand.h / 2
    handAABB["T"] = handPosition[1] + hand.h / 2

    characterAABB = {}
    characterAABB["L"] = characterPosition[0] - 25
    characterAABB["R"] = characterPosition[0] + 25
    characterAABB["B"] = characterPosition[1] - 25
    characterAABB["T"] = characterPosition[1] + 25

    if AABB(handAABB, characterAABB):
        handPosition = randPosition()
        characterVelocity = getVelocity(characterPosition[0], characterPosition[1],
                                        handPosition[0], handPosition[1], 10)

        if characterVelocity[0] < 0:
            characterFlipString = "h"
        else:
            characterFlipString = ""

    characterPosition[0] += characterVelocity[0]
    characterPosition[1] += characterVelocity[1]

    update_canvas()

    frame = (frame + 1) % 8

    delay(0.02)

close_canvas()

