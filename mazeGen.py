import util
from random import randrange, random

crxval = [10, 18]

def copy_section(stor, dat, offset_r, offset_c):
    #hor
    for r in range(len(dat['hor'])):
        for c in range(len(dat['hor'][r])):
            stor['hor'][offset_r + r][offset_c + c] = dat['hor'][r][c]
    #ver
    for r in range(len(dat['ver'])):
        for c in range(len(dat['ver'][r])):
            stor['ver'][offset_r + r][offset_c + c] = dat['ver'][r][c]

    #space
    for r in range(len(dat['space'])):
        for c in range(len(dat['space'][r])):
            stor['space'][offset_r + r][offset_c + c] = dat['space'][r][c]

def rotate_section_right(m):
    return {'hor': util.rotateright(m['ver']),
            'ver': util.rotateright(m['hor']),
            'space': util.rotateright(m['space']),
            'r_len': m['c_len'],
            'c_len': m['r_len']}

def rotate_section_left(m):
    return {'hor': util.rotateleft(m['ver']),
            'ver': util.rotateleft(m['hor']),
            'space': util.rotateleft(m['space']),
            'r_len': m['c_len'],
            'c_len': m['r_len']}

def rotate_section_half(m):
    return {'hor': util.rotatehalf(m['hor']),
            'ver': util.rotatehalf(m['ver']),
            'space': util.rotatehalf(m['space']),
            'r_len': m['r_len'],
            'c_len': m['c_len']}
    

def make_layout():
    m = {'hor': [[0 for c in range(30)] for r in range(31)],
         'ver': [[0 for c in range(31)] for r in range(30)],
         'space': [[8 for c in range(30)] for r in range(30)],
         'r_len': 30,
         'c_len': 30
        }

    cross = (crxval[randrange(2)], crxval[randrange(2)])

    m['hor'][0][cross[1]] = 2
    m['hor'][0][cross[1]+1] = 2
    m['hor'][30][cross[1]] = 2
    m['hor'][30][cross[1]+1] = 2

    m['ver'][cross[0]][0] = 2
    m['ver'][cross[0]+1][0] = 2
    m['ver'][cross[0]][30] = 2
    m['ver'][cross[0]+1][30] = 2

    if(cross[0] < 15):
        if(cross[1] < 15):
            copy_section(m, util.make_small_section(), 0, 0)
            copy_section(m, rotate_section_right(util.make_long_section()), 0, cross[1]+2)
            copy_section(m, rotate_section_left(util.make_wide_section()), cross[0]+2, 0)
            copy_section(m, rotate_section_half(util.make_large_section()), cross[0]+2, cross[1]+2)
        else:
            copy_section(m, util.make_wide_section(), 0, 0)
            copy_section(m, rotate_section_right(util.make_small_section()), 0, cross[1]+2)
            copy_section(m, rotate_section_left(util.make_large_section()), cross[0]+2, 0)
            copy_section(m, rotate_section_half(util.make_long_section()), cross[0]+2, cross[1]+2)
    else:
        if(cross[1] < 15):
            copy_section(m, util.make_long_section(), 0, 0)
            copy_section(m, rotate_section_right(util.make_large_section()), 0, cross[1]+2)
            copy_section(m, rotate_section_left(util.make_small_section()), cross[0]+2, 0)
            copy_section(m, rotate_section_half(util.make_wide_section()), cross[0]+2, cross[1]+2)
        else:
            copy_section(m, util.make_large_section(), 0, 0)
            copy_section(m, rotate_section_right(util.make_wide_section()), 0, cross[1]+2)
            copy_section(m, rotate_section_left(util.make_long_section()), cross[0]+2, 0)
            copy_section(m, rotate_section_half(util.make_small_section()), cross[0]+2, cross[1]+2)

    return m

# 0 = empty door,
# 1 = wall,
# 2 = door,
# 5 = goal,
# 6 = entrance,
# 7 = reward,
# 8 = empty,
# 9 = monster

def make_floor(l_r, l_c):
    m = {'hor': [[0 for c in range(30*l_c)] for r in range(30*l_r+1)],
         'ver': [[0 for c in range(30*l_c+1)] for r in range(30*l_r)],
         'space': [[8 for c in range(30*l_c)] for r in range(30*l_r)],
         'r_len': 30*l_r,
         'c_len': 30*l_c}

    for r in range(l_r):
        for c in range(l_c):
            copy_section(m, make_layout(), r*30, c*30)

    for c in range(m['c_len']):
        m['hor'][0][c] = 1
        m['hor'][m['r_len']][c] = 1

    for r in range(m['r_len']):
        m['ver'][r][0] = 1
        m['ver'][r][m['c_len']] = 1

    spawn_points = []
    for r in range(m['r_len']):
        for c in range(m['c_len']):
            if(m['space'][r][c] == 9):
                spawn_points.append((r, c))
    
    c = randrange(0, len(spawn_points))
    entrance = spawn_points[c]
    spawn_points = spawn_points[:c] + spawn_points[c+1:]
    m['space'][entrance[0]][entrance[1]] = 6

    c = randrange(0, len(spawn_points))
    entrance = spawn_points[c]
    spawn_points = spawn_points[:c] + spawn_points[c+1:]
    m['space'][entrance[0]][entrance[1]] = 5

    for spot in spawn_points:
        if (random() < .4):
            m['space'][spot[0]][spot[1]] = 8
        rand = random()
        if (rand < .2):
            m['space'][spot[0]][spot[1]] = 10
        elif (rand > .9):
            m['space'][spot[0]][spot[1]] = 11

    return m

ch = [(' ', ' '), ('|', '-'), ('-', '\\'), ' ', ' ', 'G', 'E', 't', ' ', 'M', 'e', 'H']

def print_floor(m):
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

m = make_floor(4, 4)

print_floor(m)

        

    
