import turtle as tr

t = tr.Turtle()
s = tr.Screen()
s.bgcolor("white")
t.pencolor("orange")

a = 0
b = 0
t.speed(10)
def xy():
    t.pensize(2)
    t.penup()
    t.setposition(0, 500)
    t.pendown()
    t.left(90)
    t.backward(1000)
    t.penup()
    t.setposition(1000, 0)
    t.pendown()
    t.right(90)
    t.backward(2000)
    t.pencolor("red")
def head():
    t.pensize(2)
    t.left(110)
    t.color("black")
    t.penup()
    t.setposition(-250, 320)
    t.pendown()
    # sol kulak
    for i in range(25):
        t.forward(8)
        t.left(1)
    t.left(90)
    for i in range(30):
        t.left(1)
        t.forward(8)
    # sol kulak end
    t.penup()
    t.setposition(-250, 320)
    t.pendown()
    t.left(115)
    # kafa üstü
    for i in range(10):
        t.forward(50)
        t.right(2.2)
    t.left(80)
    #kafa üstü end
    # sağ kulak
    for i in range(25):
        t.forward(8)
        t.right(1)
    t.right(90)
    for i in range(30):
        t.right(1)
        t.forward(8)
    # sağ kulak end
def sag():
    # sol çene
    t.penup()
    t.setposition(40, -430)
    t.pendown()
    t.left(132.77)
    for i in range(50):
        t.right(0.3)
        t.forward(10.2)
    # sol çene end
    t.right(10)
    # sol yanak
    for i in range(60):
        t.forward(6.3)
        t.left(1.5)
    # sol yanak end
def burun():
    # burun
    t.penup()
    t.setposition(40, -430)
    t.pendown()
    t.right(15)
    t.circle(40)
    # burun end
def sol():
    # sol çene
    t.penup()
    t.setposition(-38, -430)
    t.pendown()
    t.left(20)
    for i in range(50):
        t.left(0.3)
        t.forward(10.2)
    # sol çene end
    t.left(10)
    # sol yanak
    for i in range(60):
        t.forward(6.3)
        t.right(1.5)
    t.forward(28)
    # sol yanak end
xy()
head()
sag()
burun()
sol()


tr.done()