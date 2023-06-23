import turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.pensize(3)
for i in range(5):
    for colours in ["blue", "red", "violet", "yellow", "purple", "white", "orange"]:
        turtle.color(colours)

        turtle.left(12)
        for j in range(4):
            turtle.forward(200)
            turtle.left(90)
