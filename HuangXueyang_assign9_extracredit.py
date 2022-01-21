import urllib.request
import turtle

def background():
    greyscale = data[2]
    turtle.fillcolor(greyscale, greyscale, greyscale)
    turtle.pencolor(greyscale, greyscale, greyscale)
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(-(data[0]//2), data[1]//2)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(data[0])
        turtle.right(90)
        turtle.forward(data[1])
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def pixel():
    turtle.pensize(1)
    turtle.pendown()
    turtle.begin_fill()
    for c in range(4):
        turtle.forward(data[3])
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(data[3])
    
def grey(pos):
    greyscale = data[pos]
    turtle.fillcolor(greyscale, greyscale, greyscale)
    turtle.pencolor(greyscale, greyscale, greyscale)
                
def color(pos):
    red = data[pos]
    green = data[pos+1]
    blue = data[pos+2]
    turtle.fillcolor(red, green, blue)
    turtle.pencolor(red, green, blue)
    
url = input('Enter an image filename: ')
try:
    response = urllib.request.urlopen(url)
except:
    print('Sorry', url, "doesn't exist.")
else:
    data_str = response.read().decode('utf-8')
    data_str = data_str.strip()
    data = data_str.split(',')
    for i in range(len(data)):
        if data[i][0].isdigit() == True:
            data[i] = float(data[i])
        else:
            continue
    b_times = 0
    for i in data:
        if i == 'b':
            b_times += 1
    turtle.setup(data[0], data[1])
    turtle.tracer(0)
    background()
    b_iter = 0
    if data[4] == 'true':
        for i in range(5, len(data)-b_times, 3):
            if data[i] != 'b':
                color(i)
                pixel()
            else:
                del data[i]
                b_iter += 1
                turtle.goto(-(data[0]//2), (data[1]//2)-(b_iter*data[3]))
                color(i)
                pixel()
    else:
        for i in range(4, len(data)):
            if data[i] != 'b':
                grey(i)
                pixel()
            else:
                b_iter += 1
                turtle.goto(-(data[0]//2), (data[1]//2)-(b_iter*data[3]))
    turtle.update()
