# make the turtle graphics module available
import turtle

# also make the random module available
import random

# set up our graphical canvas
# width = 500, height = 500
turtle.setup(500, 500)

# set up our pen
scolor = input('Which stroke color would you like?')
if scolor == 'yellow' or scolor == 'red' or scolor == 'green' or scolor == 'blue':
    fcolor = input('Which filling color would you like?')
    if fcolor == 'yellow' or fcolor == 'red' or fcolor == 'green' or fcolor == 'blue':
        turtle.pencolor(scolor)
        turtle.pensize(2)
        turtle.fillcolor(fcolor)
        turtle.begin_fill()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
    else:
        print('Error: Color is unavailable')
        turtle.bye()        
else:
    print('Error: Color is unavailable')
    turtle.bye()


