import turtle

#setup the turtle screen
screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.bgcolor("purple")

#create a turtle for drawing
t =  turtle.Turtle()
t.color("red")
t.speed("fastest")
t.shape("turtle")
# Drawing a circle, this is a function
def draw_circle(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(size)

draw_circle(10, 10, 10)

def draw_square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)


def draw_triangle(x, y):
    
    t.penup()
    t.goto
    
    

turtle.done()