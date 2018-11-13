import turtle

def draw_square(instanceOfTurtle):
    i = 0
    while i < 4:
        instanceOfTurtle.forward(100)
        instanceOfTurtle.right(90)
        i += 1

def draw_canvas():
    window = turtle.Screen()
    window.bgcolor("green")
    #Instance of Brad Turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Instance of Angie
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    window.exitonclick()
draw_canvas()


