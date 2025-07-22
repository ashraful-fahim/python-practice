import turtle

height = 5
width = 5

turtle.speed(2)
turtle.color("blue")

turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)

turtle.exitonclick()