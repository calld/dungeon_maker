from random import randrange, random
import math

def randdiff(lvl):
    return randrange(math.ceil(9.6 + .4*lvl), math.floor(15.6 + .4*lvl))

def rotateright(m):
    temp = [[0 for r in range(len(m))] for c in range(len(m[0]))]
    for r in range(len(m)):
        for c in range(len(m[r])):
            temp[c][len(m)-r-1] = m[r][c]
    return temp

def rotateleft(m):
    temp = [[0 for r in range(len(m))] for c in range(len(m[0]))]
    for r in range(len(m)):
        for c in range(len(m[r])):
            temp[len(m[r])-1-c][r] = m[r][c]
    return temp

def rotatehalf(m):
    temp = [[0 for c in range(len(m[0]))] for r in range(len(m))]
    for r in range(len(m)):
        for c in range(len(m[r])):
            temp[len(m)-1-r][len(m[r])-1-c] = m[r][c]
    return temp

def mirror(m):
    temp = [[0 for c in range(len(m[0]))] for r in range(len(m))]
    for r in range(len(m)):
        for c in range(len(m[r])):
            temp[r][len(m[r])-1-c] = m[r][c]
    return temp


# 0 = empty,
# 1 = wall,
# 2 = door,
# 7 = reward,
# 8 = empty,
# 9 = monster

def make_small_section():
    m = {'hor': [[0 for c in range(10)] for r in range(11)],
         'ver': [[0 for c in range(11)] for r in range(10)],
         'space':[[8 for c in range(10)] for r in range(10)],
         'r_len': 10,
         'c_len': 10
        }
    cross = (randrange(4, 7), randrange(4, 7))
    # default edge
    for c in range(10):
        m['hor'][0][c] = 1
        m['ver'][c][0] = 1

    # upper left
    door = randrange(3) # 0 = both, 1 = down door, 2 = right door
    # -- right side
    for r in range(cross[0]):
        m['ver'][r][cross[1]] = 1
    if(door%2 < 1):
        m['ver'][randrange(1, cross[0]-1)][cross[1]] = 2
    # -- down side
    for c in range(cross[1]):
        m['hor'][cross[0]][c] = 1
    if(door < 2):
        m['hor'][cross[0]][randrange(1, cross[1]-1)] = 2
    if(random() < .2):
        m['space'][1][1] = 7
    m['space'][cross[0]-2][cross[1]-2] = 9

    # bottom left
    door = randrange(3)
    # -- right side
    for r in range(cross[0], len(m['ver'])):
        m['ver'][r][cross[1]] = 1
    if (door%2 < 1):
        m['ver'][randrange(cross[0] + 1, 9)][cross[1]] = 2
    # -- down side
    for c in range(cross[1]):
        m['hor'][10][c] = 1
    if (door < 2):
        m['hor'][10][randrange(1, cross[1]-1)] = 2
    if(random() < .2):
        m['space'][cross[0]+1][1] = 7
    m['space'][8][cross[1]-2] = 9

    # upper right
    door = randrange(3)
    # -- right side
    for r in range(cross[0]):
        m['ver'][r][10] = 1
    if (door%2 < 1):
        m['ver'][randrange(1, cross[0]-1)][10] = 2
    # -- down side
    for c in range(cross[1], 10):
        m['hor'][cross[0]][c] = 1
    if (door < 2):
        m['hor'][cross[0]][randrange(cross[1]+1, 9)] = 2
    if(random() < .2):
        m['space'][1][cross[1]+1] = 7
    m['space'][cross[0]-2][8] = 9

    # bottom right
    door = randrange(3)
    # -- right side
    for r in range(cross[0], 10):
        m['ver'][r][10] = 1
    if (door%2 < 1):
        m['ver'][randrange(cross[0] + 1, 9)][10] = 2
    # -- down side
    for c in range(cross[1], 10):
        m['hor'][10][c] = 1
    if (door < 2):
        m['hor'][10][randrange(cross[1]+1, 9)] = 2
    if(random() < .2):
        m['space'][cross[0]+1][cross[1]+1] = 7
    m['space'][8][8] = 9

    return m

def make_long_section():
    s = make_small_section()
    m = {'hor': [[0 for c in range(10)] for r in range(19)],
         'ver': [[0 for c in range(11)] for r in range(18)],
         'space': [[8 for c in range(10)] for r in range(18)],
         'r_len': 18,
         'c_len': 10
        }

    for r in range(10):
        for c in range(10):
            m['hor'][r][c] = s['hor'][r][c]
            m['ver'][r][c] = s['ver'][r][c]
            m['space'][r][c] = s['space'][r][c]
    for x in range(10):
        m['hor'][10][x] = s['hor'][10][x]
        m['ver'][x][10] = s['ver'][x][10]

    m['ver'][10][0] = 2
    m['ver'][11][0] = 2
    for x in range(12, 18):
        m['ver'][x][0] = 1

    cross = (randrange(12, 17), randrange(4, 7))
    for c in range(10):
        m['hor'][cross[0]][c] = 1
        m['hor'][18][c] = 1
    for r in range(10, 18):
        m['ver'][r][cross[1]] = 1
        m['ver'][r][10] = 1

    ro = random()
    # upper left room
    # -- right side
    if(ro > 1/3):
        m['ver'][randrange(11, cross[0])][cross[1]] = 2
    # -- down side
    if(ro < 2/3):
        m['hor'][cross[0]][randrange(1, cross[1])] = 2
    m['space'][cross[0]-2][cross[1]-2] = 9

    ro = random()
    # bottom left room
    # -- right side
    if(ro > 1/3):
        m['ver'][randrange(cross[0], 17)][cross[1]] = 2
    # -- down side
    if(ro < 2/3):
        m['hor'][18][randrange(0, cross[1])] = 2
    if(random() < .2):
        m['space'][cross[0]+1][1] = 7
    m['space'][16][cross[1]-2] = 9

    ro = random()
    # upper right room
    # -- right side
    if(ro > 1/3):
        m['ver'][randrange(11, cross[0])][10] = 2
    # -- down side
    if(ro < 2/3):
        m['hor'][cross[0]][randrange(cross[1], 10)] = 2
    if(random() < .2):
        m['space'][11][cross[1]+1] = 7
    m['space'][cross[0]-2][8] = 9

    ro = random()
    # bottom right room
    # -- right side
    if(ro > 1/3):
        m['ver'][randrange(cross[0], 17)][10] = 2
    # -- down side
    if(ro < 2/3):
        m['hor'][18][randrange(cross[1], 10)] = 2
    if(random() < .2):
        m['space'][cross[0]+1][cross[1]+1] = 7
    m['space'][16][8] = 9

    return m

def make_wide_section():
    m = make_long_section()
    m = {'hor': mirror(rotateright(m['ver'])),
         'ver': mirror(rotateright(m['hor'])),
         'space': mirror(rotateright(m['space'])),
         'r_len': m['c_len'],
         'c_len': m['r_len']
         }
    return m

cross_ind = [4, 5, 6, 7, 8, 9, 10, 12, 13, 14]

def make_large_section():
    m = {'hor': [[0 for c in range(18)] for r in range(19)],
         'ver': [[0 for c in range(19)] for r in range(18)],
         'space': [[8 for c in range(18)] for r in range(18)],
         'r_len': 18,
         'c_len': 18
        }

    for x in range(10):
        m['hor'][0][x] = 1
        m['ver'][x][0] = 1

    for x in range(12, 18):
        m['hor'][0][x] = 1
        m['ver'][x][0] = 1

    for x in range(10, 12):
        m['hor'][0][x] = 2
        m['ver'][x][0] = 2

    cross = (cross_ind[randrange(len(cross_ind))], cross_ind[randrange(len(cross_ind))])

    for x in range(18):
        m['hor'][18][x] = 1
        m['hor'][cross[0]][x] = 1
        m['ver'][x][18] = 1
        m['ver'][x][cross[1]] = 1

    # upper left
    rand = random()
    if(rand > 1/3):
        m['ver'][randrange(0, cross[0])][cross[1]] = 2
    if(rand < 2/3):
        m['hor'][cross[0]][randrange(0, cross[1])] = 2
    if(random() < .2):
        m['space'][1][1] = 7
    m['space'][cross[0]-2][cross[1]-2] = 9

    # bottom left
    rand = random()
    if(rand > 1/3):
        m['ver'][randrange(cross[0], 18)][cross[1]] = 2
    if(rand < 2/3):
        m['hor'][18][randrange(0, cross[1])] = 2
    if(random() < .2):
        m['space'][cross[0]+1][1] = 7
    m['space'][16][cross[1]-2] = 9

    # upper right
    rand = random()
    if(rand > 1/3):
        m['ver'][randrange(0, cross[0])][18] = 2
    if(rand < 2/3):
        m['hor'][cross[0]][randrange(cross[1], 18)] = 2
    if(random() < .2):
        m['space'][1][cross[1]+1] = 7
    m['space'][cross[0]-2][16] = 9

    #bottom right
    rand = random()
    if(rand > 1/3):
        m['ver'][randrange(cross[0], 18)][18] = 2
    if(rand < 2/3):
        m['hor'][18][randrange(cross[1], 18)] = 2
    if(random() < .2):
        m['space'][cross[0]+1][cross[1]+1] = 7
    m['space'][16][16] = 9

    return m

"""
ch = [(' ', ' '), ('|', '-'), ('-', '\\'), ' ', ' ', ' ', ' ', 't', ' ', 'M']

m = make_wide_section()
for r in range(m['r_len']):
    for c in range(m['c_len']):
        print('+ {} '.format(ch[m['hor'][r][c]][1]), end = '')
    print('+')
    for c in range(m['c_len']):
        print('{} {} '.format(ch[m['ver'][r][c]][0], ch[m['space'][r][c]]), end = '')
    print(ch[m['ver'][r][m['c_len']]][0])

for c in range(m['c_len']):
    print('+ {} '.format(ch[m['hor'][m['r_len']][c]][1]), end = '')
print('+')

ro = {
    'ver': rotateleft(m['hor']),
    'hor': rotateleft(m['ver']),
    'space': rotateleft(m['space']),
    'r_len': m['c_len'],
    'c_len': m['r_len']
    }

print('ro:')
for r in range(ro['r_len']):
    for c in range(ro['c_len']):
        print('+ {} '.format(ch[ro['hor'][r][c]][1]), end = '')
    print('+')
    for c in range(ro['c_len']):
        print('{} {} '.format(ch[ro['ver'][r][c]][0], ch[ro['space'][r][c]]), end = '')
    print(ch[ro['ver'][r][ro['c_len']]][0])

for c in range(ro['c_len']):
    print('+ {} '.format(ch[ro['hor'][ro['r_len']][c]][1]), end = '')
print('+')
"""
