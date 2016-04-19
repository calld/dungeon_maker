from random import randrange, random
import math

def randdiff(lvl):
    return randrange(math.ceil(9.6 + .4*lvl), math.floor(15.6 + .4*lvl))

def roll(n, s):
    """rolls nds"""
    return sum([randrange(1, s+1) for x in range(n)])


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
def make_p(m, coor):
    for r, c in coor:
        m['hor'][r][c] = 1
        m['hor'][r+1][c] = 1
        m['ver'][r][c] = 1
        m['ver'][r][c+1] = 1

def make_small_section():
    m = {'hor': [[0 for c in range(10)] for r in range(11)],
         'ver': [[0 for c in range(11)] for r in range(10)],
         'space':[[8 for c in range(10)] for r in range(10)],
         'r_len': 10,
         'c_len': 10
        }

    # default edge
    for c in range(10):
        m['hor'][0][c] = 1
        m['hor'][10][c] = 1
        m['ver'][c][0] = 1
        m['ver'][c][10] = 1

    t = random()

    if (t < 0.2):
        temp = [[(r, c) for c in range(1, 9)] for r in range(1, 9)]
        squares = [temp[x//8][x%8] for x in range(len(temp)*len(temp[0]))]

        for x in range(randrange(4, 17)):
            i = randrange(len(squares))
            sq = squares[i]
            squares = squares[:i] + squares[i+1:]
            m['hor'][sq[0]][sq[1]] = 1
            m['hor'][sq[0]+1][sq[1]] = 1
            m['ver'][sq[0]][sq[1]] = 1
            m['ver'][sq[0]][sq[1]+1] = 1

        make_p(m, [(0, 0), (0, 9), (9, 0), (9, 9)])

        if(random() < .5):
            m['space'][1][0] = 9
            m['space'][0][1] = 7
            m['space'][9][8] = 9
            m['space'][8][9] = 7
        else:
            m['space'][9][1] = 9
            m['space'][8][0] = 7
            m['space'][1][9] = 9
            m['space'][0][8] = 7

        door = randrange(3)
        if(door < 2):
            m['hor'][10][randrange(1,9)] = 2

        if(door%2 < 1):
            m['ver'][randrange(1,9)][10] = 2

        return m
    elif(t < 0.6):
        make_p(m, [(2, 2), (2, 7), (7, 2), (7, 7), (4, 4), (4, 5), (5, 4), (5, 5)])

        if(random() < .5):
            m['space'][1][2] = 9
            m['space'][2][1] = 7
            m['space'][8][7] = 9
            m['space'][7][8] = 7
        else:
            m['space'][8][2] = 9
            m['space'][7][1] = 7
            m['space'][1][7] = 9
            m['space'][2][8] = 7

        door = randrange(3)
        if(door < 2):
            m['hor'][10][randrange(1,9)] = 2

        if(door%2 < 1):
            m['ver'][randrange(1,9)][10] = 2

        return m

    else:
        cross = (randrange(4, 7), randrange(4, 7))
        # upper left
        door = randrange(3) # 0 = both, 1 = down door, 2 = right door
        spawns = randrange(6)
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
        if(spawns < 3):
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
        if(spawns%3 == 0 or spawns == 4):
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
        if(spawns%3 == 1 or spawns == 5):
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
        if(spawns%3 == 2 or spawns == 3):
            m['space'][cross[0]+1][cross[1]+1] = 7
            m['space'][8][8] = 9

        return m

def make_long_section():
    m = {'hor': [[0 for c in range(10)] for r in range(19)],
         'ver': [[0 for c in range(11)] for r in range(18)],
         'space': [[8 for c in range(10)] for r in range(18)],
         'r_len': 18,
         'c_len': 10
        }

    for x in range(10):
        m['hor'][0][x] = 1
        m['hor'][18][x] = 1

    for x in range(18):
        m['ver'][x][0] = 1
        m['ver'][x][10] = 1

    m['ver'][10][0] = 2
    m['ver'][11][0] = 2

    t = random()
    if(t < .2):
        make_p(m, [(2, 2), (2, 7), (6, 2), (11, 2), (15, 2), (6, 7), (11, 7), (15, 7)])

        if(random() < .5):
            m['space'][2][3] = 9
            m['space'][1][2] = 7
            m['space'][8][7] = 9
            m['space'][9][7] = 7
            m['space'][15][3] = 9
            m['space'][14][2] = 7
        else:
            m['space'][2][6] = 9
            m['space'][1][7] = 7
            m['space'][9][2] = 9
            m['space'][8][2] = 7
            m['space'][15][6] = 9
            m['space'][14][7] = 7

        door = randrange(3)
        if(door < 2):
            m['hor'][18][randrange(1,9)] = 2

        if(door%2 < 1):
            m['ver'][randrange(1,17)][10] = 2

        return m
    elif(t < .6):
        s = make_small_section()
        for r in range(10):
            for c in range(10):
                m['hor'][r][c] = s['hor'][r][c]
                m['ver'][r][c] = s['ver'][r][c]
                m['space'][r][c] = s['space'][r][c]
        for x in range(10):
            m['hor'][10][x] = s['hor'][10][x]
            m['ver'][x][10] = s['ver'][x][10]

        make_p(m, [(12, 2), (15, 2), (12, 7), (15, 7)])

        m['space'][13][4] = 9
        m['space'][14][5] = 7

        door = randrange(3)
        if(door < 2):
            m['hor'][18][randrange(1,9)] = 2

        if(door%2 < 1):
            m['ver'][randrange(11,17)][10] = 2

        return m

    else:
        s = make_small_section()
        for r in range(10):
            for c in range(10):
                m['hor'][r][c] = s['hor'][r][c]
                m['ver'][r][c] = s['ver'][r][c]
                m['space'][r][c] = s['space'][r][c]
        for x in range(10):
            m['hor'][10][x] = s['hor'][10][x]
            m['ver'][x][10] = s['ver'][x][10]

        cross = (14, randrange(4, 7))
        for c in range(10):
            m['hor'][cross[0]][c] = 1
            m['hor'][18][c] = 1
        for r in range(10, 18):
            m['ver'][r][cross[1]] = 1
            m['ver'][r][10] = 1

        ro = random()
        d = randrange(4)
        # upper left room
        # -- right side
        if(ro > 1/3):
            m['ver'][randrange(11, cross[0])][cross[1]] = 2
        # -- down side
        if(ro < 2/3):
            m['hor'][cross[0]][randrange(1, cross[1])] = 2
        if(d == 0):
            m['space'][11][1] = 7
            m['space'][cross[0]-2][cross[1]-2] = 9

        ro = random()
        # bottom left room
        # -- right side
        if(ro > 1/3):
            m['ver'][randrange(cross[0], 17)][cross[1]] = 2
        # -- down side
        if(ro < 2/3):
            m['hor'][18][randrange(0, cross[1])] = 2
        if(d == 1):
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
        if(d == 2):
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
        if(d == 3):
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

    for x in range(18):
        m['hor'][18][x] = 1
        m['ver'][x][18] = 1

    t = random()
    if(t < 0.2):
        s = make_small_section();

        for c in range(10):
            for r in range(10):
                m['hor'][r+4][c+4] = s['hor'][r][c]
                m['ver'][r+4][c+4] = s['ver'][r][c]
                m['space'][r+4][c+4] = s['space'][r][c]

        for x in range(10):
            m['hor'][14][x+4] = s['hor'][10][x]
            m['ver'][x+4][14] = s['ver'][x][10]

        m['hor'][4][randrange(5, 13)] = 2
        m['ver'][randrange(5, 13)][4] = 2

        if(random() < .5):
            m['space'][2][2] = 9
            m['space'][1][1] = 7
            m['space'][15][15] = 7
            m['space'][16][16] = 9
        else:
            m['space'][16][1] = 9
            m['space'][15][2] = 7
            m['space'][1][16] = 7
            m['space'][2][15] = 9

        m['hor'][18][randrange(2, 16)] = 2
        m['ver'][randrange(2, 16)][18] = 2

        return m
    
    elif(t < 0.6):
        make_p(m, [(0, 0), (1, 1), (0, 17), (1, 16), (17, 0), (16, 1), (17, 17), (16, 16)])

        maze_rows = [[(r, c) for c in range(2, 16)] for r in range(2, 16)]

        make_p(m, [maze_rows[x//14][x%14] for x in range(len(maze_rows)*len(maze_rows[0]))])

        crp = []
        # [upper, left, down, right]
        if(random() < .5):
            cross = [(randrange(3, 8), randrange(3, 8)), (randrange(9, 14), randrange(9, 14))]
            crp.append(cross[1])
            crp.append(cross[1])
            crp.append(cross[0])
            crp.append(cross[0])
        else:
            cross = [(randrange(3, 8), randrange(9, 14)), (randrange(9, 14), randrange(3, 8))]
            crp.append(cross[1])
            crp.append(cross[0])
            crp.append(cross[0])
            crp.append(cross[1])

        #upper
        for r in range(2, crp[0][0]+2):
            m['hor'][r][crp[0][1]] = 0
            m['hor'][r][crp[0][1]+1] = 0
            m['ver'][r][crp[0][1]+1] = 0

        #left
        for c in range(2, crp[1][1]+2):
            m['ver'][crp[1][0]][c] = 0
            m['ver'][crp[1][0]+1][c] = 0
            m['hor'][crp[1][0]+1][c] = 0

        #down
        for r in range(crp[2][0]+1, 17):
            m['hor'][r][crp[2][1]] = 0
            m['hor'][r][crp[2][1]+1] = 0
            m['ver'][r-1][crp[2][1]+1] = 0

        #right
        for c in range(crp[3][1]+1, 17):
            m['ver'][crp[3][0]][c] = 0
            m['ver'][crp[3][0]+1][c] = 0
            m['hor'][crp[3][0]+1][c-1] = 0

        m['hor'][18][randrange(2, 16)] = 2
        m['ver'][randrange(2, 16)][18] = 2

        m['space'][1][10] = 9
        m['space'][1][7] = 7
        m['space'][7][1] = 9
        m['space'][10][1] = 7
        m['space'][16][7] = 9
        m['space'][16][10] = 7
        m['space'][7][16] = 7
        m['space'][10][16] = 9

        return m
    else:
        cross = (cross_ind[randrange(len(cross_ind))], cross_ind[randrange(len(cross_ind))])

        for x in range(18):
            m['hor'][cross[0]][x] = 1
            m['ver'][x][cross[1]] = 1

        # upper left
        rand = random()
        if(rand > 1/3):
            m['ver'][randrange(0, cross[0])][cross[1]] = 2
        if(rand < 2/3):
            m['hor'][cross[0]][randrange(0, cross[1])] = 2
        m['space'][1][1] = 7
        m['space'][cross[0]-2][cross[1]-2] = 9

        # bottom left
        rand = random()
        if(rand > 1/3):
            m['ver'][randrange(cross[0], 18)][cross[1]] = 2
        if(rand < 2/3):
            m['hor'][18][randrange(0, cross[1])] = 2
        m['space'][cross[0]+1][1] = 7
        m['space'][16][cross[1]-2] = 9

        # upper right
        rand = random()
        if(rand > 1/3):
            m['ver'][randrange(0, cross[0])][18] = 2
        if(rand < 2/3):
            m['hor'][cross[0]][randrange(cross[1], 18)] = 2
        m['space'][1][cross[1]+1] = 7
        m['space'][cross[0]-2][16] = 9

        #bottom right
        rand = random()
        if(rand > 1/3):
            m['ver'][randrange(cross[0], 18)][18] = 2
        if(rand < 2/3):
            m['hor'][18][randrange(cross[1], 18)] = 2
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
