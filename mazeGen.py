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

    for x in range(30):
        if (x == 10 or x == 11 or x == 18 or x == 19):
            m['hor'][0][x] = 2
            m['hor'][30][x] = 2
            m['ver'][x][0] = 2
            m['ver'][x][30] = 2
        else:
            m['hor'][0][x] = 1
            m['hor'][30][x] = 1
            m['ver'][x][0] = 1
            m['ver'][x][30] = 1
    
    layType = random()
    rotate = []
    f = lambda x: x
    rotate.append(f)
    f = lambda x: rotate_section_right(x)
    rotate.append(f)
    f = lambda x: rotate_section_half(x)
    rotate.append(f)
    f = lambda x: rotate_section_left(x)
    rotate.append(f)
    if(layType < .16666):
        f = lambda: util.make_small_section()
        #4 10s, floating
        copy_section(m, rotate[randrange(4)](f()), 4, 4)
        copy_section(m, rotate[randrange(4)](f()), 4, 16)
        copy_section(m, rotate[randrange(4)](f()), 16, 4)
        copy_section(m, rotate[randrange(4)](f()), 16, 16)

        m['space'][1][1] = 9
        m['space'][1][28] = 9
        m['space'][28][1] = 9
        m['space'][28][28] = 9
        m['space'][14][14] = 7

    elif(layType < .33333):
        # 4 10s, inner cross
        copy_section(m, rotate[0](util.make_small_section()), 0, 0)
        copy_section(m, rotate[1](util.make_small_section()), 0, 20)
        copy_section(m, rotate[2](util.make_small_section()), 20, 0)
        copy_section(m, rotate[3](util.make_small_section()), 20, 20)

        #inner hall edge
        for x in range(12, 18):
            m['hor'][2][x] = 1
            m['hor'][28][x] = 1
            m['ver'][x][2] = 1
            m['ver'][x][28] = 1
        for x in range(2, 12):
            m['ver'][x][12] = 1
            m['ver'][29-x][12] = 1
            m['ver'][x][18] = 1
            m['ver'][29-x][18] = 1
            m['hor'][12][x] = 1
            m['hor'][12][29-x] = 1
            m['hor'][18][x] = 1
            m['hor'][18][29-x] = 1

        temp = [[(r, c) for c in range(13, 17)] for r in range(3, 11)] + [[(r, c) for c in range(3, 27)] for r in range(13, 17)] + [[(r, c) for c in range(13, 17)] for r in range(19, 27)]

        points = []
        for row in temp:
            points.extend(row)

        #random columns
        util.make_p(m, [points.pop(randrange(len(points))) for x in range(randrange(10, 21))])

        #spawn points
        jump = len(points)//5

        i = []
        i.append(randrange(jump//2, jump))
        i.append(i[-1] + randrange((jump*3)//4, (jump*3)//2) - 2)
        i.append(i[-1] + randrange((jump*3)//4, jump) - 4)
        i.append(i[-1] + randrange((jump*3)//4, (jump*3)//2) - 6)
        
        for x in i:
            m['space'][points[x][0]][points[x][1]] = 9
            m['space'][points[x+2][0]][points[x+2][1]] = 7
            points.pop(x)
            points.pop(x+1)

        #doors

        fulldoors = [['ver', randrange(3, 11), 12], ['ver', randrange(3, 11), 18], ['ver', randrange(19, 27), 12], ['ver', randrange(19, 27), 18],
                     ['hor', 12, randrange(3, 11)], ['hor', 18, randrange(3, 11)], ['hor', 12, randrange(19, 27)], ['hor', 18, randrange(19, 27)]]

        for door in [fulldoors.pop(randrange(len(fulldoors))) for x in range(randrange(2, 5))]:
            m[door[0]][door[1]][door[2]] = 2
        
    elif(layType < .5):
        i = randrange(2)
        j = 1 - i
        f = [lambda: util.make_long_section(), lambda: util.make_wide_section()][i]
        #4 18s
        copy_section(m, rotate[0](f()), 0, 0)
        copy_section(m, rotate[1](f()), 0, crxval[i]+2)
        copy_section(m, rotate[2](f()), crxval[i]+2, crxval[j]+2)
        copy_section(m, rotate[3](f()), crxval[j]+2, 0)

        m['space'][14][14] = 9
        
    elif(layType < .66666):
        i = randrange(2)
        f = [lambda: util.make_long_section(), lambda: util.make_wide_section()][i]
        #30, 2 10s, 18
        copy_section(m, rotate[0](util.make_large_section()), 0, 0)
        copy_section(m, rotate[1](util.make_small_section()), 0, 20)
        copy_section(m, rotate[2](f()), (12, 20)[i], (20, 12)[i])
        copy_section(m, rotate[3](util.make_small_section()), 20, 0)

        m['space'][(21,13)[i]][(13,21)[i]] = 9

        m = rotate[randrange(4)](m)
    elif(layType < .83333):
        # 5 10's, checkerboard
        i = randrange(4)
        copy_section(m, rotate[0](util.make_small_section()), 0, 0)
        copy_section(m, rotate[1](util.make_small_section()), 0, 20)
        copy_section(m, rotate[2](util.make_small_section()), 20, 20)
        copy_section(m, rotate[3](util.make_small_section()), 20, 0)
        copy_section(m, util.make_small_section(), 10, 10)

        t = randrange(3)
        if(t < 2):
            m['hor'][10][randrange(11, 19)] = 2

        if(t%2 == 0):
            m['ver'][randrange(11, 19)][10] = 2

        m['space'][3][13] = 9
        m['space'][6][16] = 7
        m['space'][13][3] = 9
        m['space'][16][6] = 7
        m['space'][13][23] = 9
        m['space'][16][26] = 7
        m['space'][23][13] = 9
        m['space'][26][16] = 7

        m = rotate[randrange(4)](m)
        
    else:
        cross = (crxval[randrange(2)], crxval[randrange(2)])
        
        m['space'][cross[0]][cross[1]] = 9

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

    opensp = []
    for r in range(30):
        opensp.append([])
        for c in range(30):
            if(m['space'][r][c] == 8):
                opensp[r].append((r, c))
    
    for x in range(randrange(4)):
        r = randrange(30)
        m['space'][r][opensp[r][randrange(len(opensp[r]))][1]] = 13
        #print('trap made')

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
        rand = random()
        if (rand < .2):
            m['space'][spot[0]][spot[1]] = 8
        elif(rand < .59):
            m['space'][spot[0]][spot[1]] = 10
        elif(rand < .902):
            m['space'][spot[0]][spot[1]] = 9
        elif(rand < .98):
            m['space'][spot[0]][spot[1]] = 11
        else:
            m['space'][spot[0]][spot[1]] = 12

    reSp = []
    for r in range(m['r_len']):
        for c in range(m['c_len']):
            if(m['space'][r][c] == 7):
                reSp.append((r, c))

    c = randrange(0, len(reSp))
    horde = reSp[c]
    reSp = reSp[:c] + reSp[c+1:]
    m['space'][horde[0]][horde[1]] = 4

    c = randrange(0, len(reSp))
    horde = reSp[c]
    reSp = reSp[:c] + reSp[c+1:]
    m['space'][horde[0]][horde[1]] = 4

    for spot in reSp:
        if(random() < .2):
            m['space'][spot[0]][spot[1]] = 8

    vdoors = []
    hdoors = []
    for r in range(m['r_len']):
        for c in range(m['c_len']):
            if (m['ver'][r][c] == 2):
                vdoors.append((r, c))
            if (m['hor'][r][c] == 2):
                hdoors.append((r, c))

    for door in vdoors:
        if(random() < .15 and not chkBD(door, m)):
            m['ver'][door[0]][door[1]] = 3

    for door in hdoors:
        if(random() < .15 and not chkBD(door, m)):
            m['hor'][door[0]][door[1]] = 3

    return m


def chkBD(pos, m):
    """pos[0] = r, p[1] = c checks if position is adjecent to a door, m is the map"""
    cur = False
    for x in [-1, 1]:
        if(pos[0] + x >= 0 and pos[0] + x < m['r_len']):
            cur = cur or m['ver'][pos[0]+x][pos[1]] == 2
        if(pos[1] + x >= 0 and pos[1] + x < m['c_len']):
            cur = cur or m['hor'][pos[0]][pos[1]+x] == 2

    return cur

ch = [(' ', ' '), ('|', '-'), ('-', '\\'),
      ('S','S'), 'T', 'G', 'E', 't', ' ', 'M', 'e', 'H', 'P']


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
