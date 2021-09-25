import turtle
t = turtle.Turtle()
import random
r = random.Random()
def stvorec(dlzka):
     for i in range(4) :
         t.fd(dlzka)
         t.rt(90)

def trojuholnik(dlzka):
    for i in range(3) :
        t.fd(dlzka)
        t.rt(120)

def umiestennie():
    t.pu()
    t.setpos(random.randrange(-250, 250)
             random.randrange(-250, 250))
    t.seth(random.randrange(360))
    t.pd()

    turtle.delay(0)
t.pensize(8)
for i in range(20) :
    umiestennie()
    if random.randrange(2):
        t.pencolor('green')
        stvorec(random.randrange(15, 120))
    else:
        t.pencolor('yellow')
        trojuholnik(random.randrange(15, 120))

turtle.exitonclick()

