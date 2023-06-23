import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
color1 = ["yellow", "green", "red", "blue"]
t.up()
t.goto(100, 50)
for i in range(4):
    t.down()
    t.color(color1[i])
    t.pensize(10)

    t.circle(75)

    t.up()
    t.bk(77)
