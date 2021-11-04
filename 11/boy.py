from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, DASH_DOWN, DASH_UP, DASH_END_TIMER = range(8)

class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 100

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 80
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame // 10 * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame // 10 * 100, 200, 100, 100, boy.x, boy.y)

class SleepState:
    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 80

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame // 10 * 100, 300, 100, 100,
            3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame // 10 * 100, 200, 100, 100,
            -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 40
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 -25)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame // 5 * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame // 5 * 100, 0, 100, 100, boy.x, boy.y)

class DashState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity
        boy.timer = 100

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 24
        boy.timer -= 1
        boy.x += boy.velocity * 3
        boy.x = clamp(25, boy.x, 800 -25)
        if boy.timer == 0:
            boy.add_event(DASH_END_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame // 3 * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame // 3 * 100, 0, 100, 100, boy.x, boy.y)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT): DASH_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_LSHIFT): DASH_UP
}

next_state_table = {
    IdleState: {
        RIGHT_UP: RunState,
        LEFT_UP: RunState,
        DASH_DOWN: IdleState,
        RIGHT_DOWN: RunState,
        LEFT_DOWN: RunState,
        DASH_UP: IdleState,
        SLEEP_TIMER: SleepState
    },
    RunState: {
        RIGHT_UP: IdleState,
        LEFT_UP: IdleState,
        LEFT_DOWN: IdleState,
        DASH_UP: RunState,
        RIGHT_DOWN: IdleState,
        DASH_DOWN: DashState
    },
    SleepState: {
        LEFT_DOWN: RunState,
        RIGHT_DOWN: RunState,
        DASH_DOWN: IdleState,
        LEFT_UP: RunState,
        RIGHT_UP: RunState,
        DASH_UP: IdleState
    },
    DashState: {
        RIGHT_UP: IdleState,
        LEFT_UP: IdleState,
        DASH_UP: RunState,
        LEFT_DOWN: IdleState,
        RIGHT_DOWN: IdleState,
        DASH_DOWN: RunState,
        DASH_END_TIMER: RunState
    },
}

class Boy:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0

        self.eventQueue = []
        self.currentState = IdleState
        self.currentState.enter(self, None)

    def add_event(self, event):
        self.eventQueue.insert(0, event)

    def update(self):
        self.currentState.do(self)

        if len(self.eventQueue) > 0:
            event = self.eventQueue.pop()
            self.currentState.exit(self, event)
            self.currentState = next_state_table[self.currentState][event]
            self.currentState.enter(self, event)

    def draw(self):
        debug_print(str(self.x) + " " + str(self.y) + " " + str(self.currentState))
        self.currentState.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)