import turtle

x, y = 0, 0

def move_up():
    global x, y
    y += 50
    turtle.setheading(90)
    turtle.goto(x, y)
    turtle.stamp()

def move_left():
    global x, y
    x -= 50
    turtle.setheading(180)
    turtle.goto(x, y)
    turtle.stamp()

def move_right():
    global x, y
    x += 50
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.stamp()

def move_down():
    global x, y
    y -= 50
    turtle.setheading(270)
    turtle.goto(x, y)
    turtle.stamp()

def reset():
    global x, y
    turtle.reset()
    turtle.stamp()
    x, y = 0, 0

turtle.shape('turtle')
turtle.stamp()

turtle.onkey(move_up, 'w')
turtle.onkey(move_down, 's')
turtle.onkey(move_left, 'a')
turtle.onkey(move_right, 'd')
turtle.onkey(reset, 'Escape')
turtle.listen()