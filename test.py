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

pure_goto(mideana)

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
    pure_goto(position)

def letter_J():
    position = pos()
    pure_goto(pos() + vector_up)
    goto(pos() + vector_down + (vector_right[0] / 2, vector_right[1] / 2)) 
    goto(pos() + vector_up + (vector_right[0] / 2, vector_right[1] / 2))
    pure_goto(position)

def letter_W():
    position = pos()
    pure_goto(pos() + vector_up)
    goto(pos() + vector_down + (vector_right[0] / 2, vector_right[1] / 2)) 
    goto(pos() + vector_up + (vector_right[0] / 2, vector_right[1] / 2))
    pure_goto(position)
    center_dot(15)
       
def letter_X():
    position = pos()
    goto(pos() + vector_up + (vector_right[0] / 2, vector_right[1] / 2)) 
    goto(pos() + vector_down + (vector_right[0] / 2, vector_right[1] / 2))
    pure_goto(position)
    center_dot(15)

def letter_L():
    position = pos()
    goto(pos() + vector_right + (vector_up[0] / 2, vector_up[1] / 2 )) 
    goto(pos() + vector_left + (vector_up[0] / 2, vector_up[1] / 2 ))
    pure_goto(position)

def letter_Y():
    position = pos()
    goto(pos() + vector_right + (vector_up[0] / 2, vector_up[1] / 2 )) 
    goto(pos() + vector_left + (vector_up[0] / 2, vector_up[1] / 2 ))
    pure_goto(position)
    center_dot(15)

def letter_M():
    position = pos()
    pure_goto(pos() + vector_right)
    goto(pos() + vector_left + (vector_up[0] / 2, vector_up[1] / 2 )) 
    goto(pos() + vector_right + (vector_up[0] / 2, vector_up[1] / 2 ))
    pure_goto(position)

def letter_Z():
    position = pos()
    pure_goto(pos() + vector_right)
    goto(pos() + vector_left + (vector_up[0] / 2, vector_up[1] / 2 )) 
    goto(pos() + vector_right + (vector_up[0] / 2, vector_up[1] / 2 ))
    pure_goto(position)
    center_dot(15)

def letter_A():
    down_line()
    right_line()

def letter_B():
    left_line()
    down_line()
    right_line()

def letter_O():
    left_line()
    down_line()
    right_line()
    center_dot(15)

def letter_C():
    left_line()
    down_line()

def letter_P():
    left_line()
    down_line()
    center_dot(15)

def letter_D():
    down_line()
    upper_line()
    right_line()

def letter_E():
    down_line()
    upper_line()
    right_line()
    left_line()

def letter_R():
    down_line()
    upper_line()
    right_line()
    left_line()
    center_dot(15)

def letter_F():
    down_line()
    upper_line()
    left_line()
    
def letter_S():
    down_line()
    upper_line()
    left_line()
    center_dot(15)

def letter_Q():
    down_line()
    upper_line()
    right_line()
    center_dot(15)

def letter_N():
    down_line()
    right_line()
    center_dot(15)

def letter_G():
    upper_line()
    right_line()
    
def letter_T():
    upper_line()
    right_line()
    center_dot(15)

def letter_H():
    upper_line()
    right_line()
    left_line()

def letter_U():
    upper_line()
    right_line()
    left_line()
    center_dot(15)

def letter_I():
    upper_line()
    left_line()

def letter_V():  
    upper_line()
    left_line()
    center_dot(15)

def exec_letter(letter):
    current_funk = "letter_" + letter
    if current_funk in globals():
        globals()[current_funk]()


def encript(text):
    text = text.upper()
    for letter in text:
        exec_letter(letter)
        position = pos()
        pure_goto(position + vector_right + (letter_speceing, 0))

encript("MISha")


input()




