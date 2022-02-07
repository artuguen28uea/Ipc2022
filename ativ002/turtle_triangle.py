import turtle

wn = turtle.Screen()

tess = turtle.Turtle()


def triangle(x, y):

    tess.penup()

    tess.goto(x, y)

    tess.pendown()
    for i in range(3):
        tess.forward(100)

        tess.left(120)

        tess.forward(100)


turtle.onscreenclick(triangle, 1)

turtle.listen()

turtle.done()
