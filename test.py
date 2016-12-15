from turtle import *
border = 20
letter_size = 100
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

def center_dot(size):
    position = pos()
    pure_goto(position + (letter_size / 2, letter_size / 2))
    dot(size)
    pure_goto(position)

def down_line():
    position = pos()
    goto(pos() + (vector_right))
    pure_goto(position)

def upper_line():
    position = pos()
    pure_goto(pos() + vector_up)
    goto(pos() + vector_right)
    pure_goto(position) 
    
def left_line():
    position = pos()
    goto (pos() + vector_up)
    pure_goto(position)

def right_line():
    position = pos()
    pure_goto (pos() + vector_right)
    goto (pos() + vector_up)
    pure_goto(position)

def letter_K():
    position = pos()

    goto(pos() + vector_up + (vector_right[0] / 2, vector_right[1] / 2)) 
    goto(pos() + vector_down + (vector_right[0] / 2, vector_right[1] / 2))

def letter_A():
    down_line()
    right_line()

def letter_N():
    down_line()
    right_line()
    center_dot(15)

pure_goto(mideana)
letter_A()
letter_N()
letter_K()
input()




