from turtle import *
border = 15
letter_size = 30
letter_speceing = 20
size = [800, 600]
mideana =[0, 0] 
mideana[0] = - size[0] / 2 + border 
mideana[1] = size[1] / 2 - border - letter_size
setup(*size)
bgcolor("lightgray")
color("blue")
width(4)

vector_up = (0, 100)
vector_down = (0, -100)
vector_left = (-100,0)
vector_right = (100,0)

def pure_turtle(action):
    up()
    action()
    down()

def pure_goto(point):
    pure_turtle(lambda: goto(point))

pure_goto(mideana)
goto(pos() + vector_right)

input()




