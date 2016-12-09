from turtle import *
border = 15
size = [800, 600]
mideana =[0, 0] 
mideana[0] = - size[0] / 2 + border
mideana[1] = size[1] / 2 - border
setup(*size)
bgcolor("lightgreen")
color("blue")
goto(mideana)

commands_list = {
    "f": fd,
    "b": bk,
    "l": lt,
    "r": rt,  
}

def magic_split(string,spiter):
    return [substring.strip() for substring in string.strip().split(spiter)]


def exec_comand(comand):
    name, param = magic_split(comand, " ")
    commands_list[name](int(param))

def interpreter(commands):
    commands = magic_split(commands, ",")
    for command in commands:
        exec_comand(command)

def generete_dictionary(file_name):
    letters = {}
    with open(file_name,"r") as f:
        for line in f:
            letter, commands = magic_split(line, ":")
            letters[letter] = commands
    return letters

letters = generete_dictionary("dict.txt")




word = "Cbbccbbch"
def interprin_word (word):
    for letter in word.lower():
        if letter not in letters.keys():
            continue
        interpreter(letters[letter])

#interprin_word(word)


# interpreter(letters["b"])
# interpreter(letters["c"])
# interpreter(letters["c"])
# interpreter(letters["b"])

input()


       




