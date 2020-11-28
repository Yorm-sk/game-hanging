# here are our algoritm for game
symb = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def calc(i):
    i -= 1
    return  i

def check(letter):
    if letter not in symb:
        return False