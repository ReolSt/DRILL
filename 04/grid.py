import turtle

turtle.setup(800, 800)

turtle.penup()
turtle.goto(-250, 250)

for i in range(6):
    turtle.penup()
    turtle.goto(-250, 250 - i * 100)
    turtle.pendown()
    turtle.forward(500)

turtle.penup()
turtle.goto(-250, 250)
turtle.right(90)

for i in range(6):
    turtle.penup()
    turtle.goto(-250 + i * 100, 250)
    turtle.pendown()
    turtle.forward(500)

turtle.exitonclick()