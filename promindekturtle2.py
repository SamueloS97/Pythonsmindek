import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()


class Shape:
    color = None

    def __init__(self, color):
        self.color = color

    def draw(self):
        turtle.home()
        turtle.pencolor(self.color)

    def setColor(self, color):
        self.color = color


class Rectangle(Shape):
    def draw(self):
        Shape.draw(self)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)


class Triangle(Shape):
    def draw(self):
        Shape.draw(self)
        turtle.left(60)
        turtle.forward(200)
        turtle.right(120)
        turtle.forward(200)
        turtle.right(120)
        turtle.forward(200)


class Circle(Shape):
    def draw(self):
        Shape.draw(self)
        turtle.circle(200)


rectangle = Rectangle(color="green")
triangle = Triangle(color="red")
circle = Circle(color="blue")

rectangle.draw()
triangle.draw()
circle.draw()

screen.exitonclick()