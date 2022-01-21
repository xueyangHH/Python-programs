# Name: Xueyang Huang
# Date: February 19th
# Class section: 02
# Name of program: HuangXueyang_assign3_problem1.py

# import math module
import math

# title
print('Valid Triangle Tester')

# ask the user for 3 points
# p.s. when you are entering the points, please make sure that your numbers are
# large enough (i.e. x > 20) but smaller than 250 because I am setting the canvas
# range to be (500, 500). That means if the values you entered for those points
# are too small, you could hardly see the triangle; and if they are too
# large, you wouldn't be able to see them on the canvas as well
point1_x = round(float(input('\nEnter Point #1 - x position: ')), 2)
point1_y = round(float(input('Enter Point #1 - y position: ')), 2)
point2_x = round(float(input('Enter Point #2 - x position: ')), 2)
point2_y = round(float(input('Enter Point #2 - y position: ')), 2)
point3_x = round(float(input('Enter Point #3 - x position: ')), 2)
point3_y = round(float(input('Enter Point #3 - y position: ')), 2)

# compute the distance between each point
dist1_2 = round(math.sqrt((point1_x - point2_x) ** 2 + (point1_y - point2_y) ** 2), 2)
dist1_3 = round(math.sqrt((point1_x - point3_x) ** 2 + (point1_y - point3_y) ** 2), 2)
dist2_3 = round(math.sqrt((point2_x - point3_x) ** 2 + (point2_y - point3_y) ** 2), 2)

# format and print out the distance
print('\nThe length of each side of your test shape is:')
print('\nSide 1:', format(dist1_2, '.2f'))
print('Side 2:', format(dist1_3, '.2f'))
print('Side 3:', format(dist2_3, '.2f'))

# determine if the shape is a triangle
if (dist1_2 + dist1_3 > dist2_3 and dist1_3 + dist2_3 > dist1_2
    and dist2_3 + dist1_2 > dist1_3):
    print('\nThis is a valid triangle!')
    # determine the type of the triangle
    # if all of the sides have the same length, it is equilateral
    # draw the triangle in turtle graphics
    if dist1_2 == dist1_3 == dist2_3:
        print('This is an equilateral triangle!')
        import turtle
        turtle.setup(500,500)
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(point1_x, point1_y)
        turtle.pencolor('green')
        turtle.pendown()
        turtle.goto(point2_x, point2_y)
        turtle.goto(point3_x, point3_y)
        turtle.goto(point1_x, point1_y)
        turtle.penup()       
    else:
        # if two of the sides have the same length, it is isosceles
        # draw the triangle in turtle graphics
        if dist1_2 == dist1_3 or dist1_3 == dist2_3 or dist1_2 == dist2_3:
            print('This is an isosceles triangle!')
            import turtle
            turtle.setup(500,500)
            turtle.pensize(5)
            turtle.penup()
            turtle.goto(point1_x, point1_y)
            turtle.pencolor('blue')
            turtle.pendown()
            turtle.goto(point2_x, point2_y)
            turtle.goto(point3_x, point3_y)
            turtle.goto(point1_x, point1_y)
            turtle.penup()
        else:
            # if none of the sides have the same length, it is scalene
            # draw the triangle in turtle graphics
            print('This is a scalene triangle!')
            import turtle
            turtle.setup(500,500)
            turtle.pensize(5)
            turtle.penup()
            turtle.goto(point1_x, point1_y)
            turtle.pencolor('red')
            turtle.pendown()
            turtle.goto(point2_x, point2_y)
            turtle.goto(point3_x, point3_y)
            turtle.goto(point1_x, point1_y)
            turtle.penup()
else:
    print('\nThis is not a valid triangle!')
