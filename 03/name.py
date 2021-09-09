import turtle

turtle.write("정수민", font=("Arial", 50, 'normal'))

commands = [
    # ㅈ
    ('f', 100), ('r', 130), ('f', 150), ('u'), ('b', 75), ('d'), ('l', 80), ('f', 75), ('l', 140),
    # move for next syllable
    ('u'), ('f', 50), ('l', 90), ('f', 20), ('d'),
    # ㅓ
    ('b', 50), ('r', 90), ('u'), ('f', 70), ('d'), ('b', 140),
    # move for next syllable
    ('u'), ('l', 90), ('f', 50),
    # ㅇ
    ('d'), ('c', 40),
    # move for next character
    ('u'), ('b', 100), ('r', 90), ('f', 20),
    # ㅅ
    ('d'), ('r', 30), ('f', 130), ('l', 60), ('b', 130),
    # move for next syllable
    ('r', 30), ('u'), ('b', 20), ('l', 90), ('f', 140),
    # ㅜ
    ('d'), ('b', 160), ('u'), ('f', 80), ('l', 90), ('d'), ('f', 80),
    # move for next character
    ('u'), ('b', 210), ('l', 90), ('f', 100),
    # ㅁ
    ('d'), ('f', 100), ('r', 90), ('f', 100), ('r', 90), ('f', 100), ('r', 90), ('f', 100), ('r', 90),
    # move for next syllable
    ('u'), ('f', 120), ('l', 90), ('f', 20),
    # ㅣ
    ('d'), ('b', 140),
    # move for next syllable
    ('u'), ('l', 90), ('f', 100),
    # ㄴ
    ('l', 90), ('d'), ('f', 80), ('l', 90), ('f', 120)]

turtle.penup()
turtle.goto((-300, 300))
turtle.pendown()

for command in commands:
    c = command[0]
    if c == 'u':
        turtle.penup()
    elif c == 'd':
        turtle.pendown()
    elif c == 'f':
        v = command[1]
        turtle.forward(v)
    elif c == 'b':
        v = command[1]
        turtle.backward(v)
    elif c == 'l':
        v = command[1]
        turtle.left(v)
    elif c == 'r':
        v = command[1]
        turtle.right(v)
    elif c == 'c':
        v = command[1]
        turtle.circle(v)

turtle.exitonclick()