import turtle as tr

t = tr.Turtle()
s = tr.Screen()
s.bgcolor("black")
tr.pencolor("green")

a = 0
b = 0
tr.speed(0)
tr.penup()
tr.goto(0, -200)
tr.pendown()

while True:
    tr.forward(a)
    tr.left(b)
    a = a+3
    b = b+1
    if b == 210:
        break
    tr.hideturtle()

tr.done()