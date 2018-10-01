import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.color("yellow")
    
    i = 0
    while i < 4:
        brad.forward(100)
        brad.right(90)
        i += 1
        
draw_square()

def draw_circle():
    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(60)
    
draw_circle()


window.exitonclick()
