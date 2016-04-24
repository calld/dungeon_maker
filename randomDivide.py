from random import randrange, random

def randDivideLayout():
    m = {
        'hor': [[0 for c in range(30)] for r in range(31)],
        'ver': [[0 for c in range(31)] for r in range(30)],
        'space': [[8 for c in range(30)] for r in range(30)],
        'r_len': 30,
        'c_len': 30
        }

    for x in range(30):
        v = 1
        if(x == 10 or x == 11 or x == 18 or x == 19):
            v = 2
        m['hor'][0][x] = v
        m['hor'][30][x] = v
        m['ver'][x][0] = v
        m['ver'][x][30] = v
