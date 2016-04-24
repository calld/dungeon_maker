from random import randrange, random

def randstart(m):
    openspots = []
    for r in range(m['r_len']+1):
        for c in range(m['c_len']):
            if(m['hor'][r][c] == 0):
                openspots.append(('hor', r, c))

    for r in range(m['r_len']):
        for c in range(m['c_len']+1):
            if(m['ver'][r][c] == 0):
                openspots.append(('ver', r, c))

    selected = openspots[randrange(len(openspots))]
    m[selected[0]][selected[1]][selected[2]] = 1
    if(selected[0] == 'hor'):
        if(random() < .5):
            return (selected[1], selected[2], 'west')
        else:
            return (selected[1], selected[2], 'east')
    else:
        if(random() < .5):
            return (selected[1], selected[2], 'north')
        else:
            return (selected[1]+1, selected[2], 'south')


def getInnerDensity(m):
    spacecount = 0
    filledcount = 0

    for r in range(1, 30):
        for c in range(30):
            if(m['hor'][r][c] == 0):
                spacecount = spacecount + 1
            else:
                filledcount = filledcount + 1

    for r in range(30):
        for c in range(1, 30):
            if(m['ver'][r][c] == 0):
                spacecount = spacecount + 1
            else:
                filledcount = filledcount + 1

    return filledcount/(spacecount + filledcount)

def standardWall(i):
    if(i == 10 or i == 11 or i == 18 or i == 19):
        return 2
    else:
        return 1

def getwallopt(m, cur):
    r = []
    if(cur[0] == 0 or cur[0] == m['r_len'] or cur[1] == 0 or cur[1] == m['c_len']):
        return r
    
    if(cur[2] != 'north'):
        r.append((('ver', cur[0], cur[1]), (cur[0]+1, cur[1], 'south')))

    if(cur[2] != 'west'):
        r.append((('hor', cur[0], cur[1]), (cur[0], cur[1], 'east')))

    if(cur[2] != 'south'):
        r.append((('ver', cur[0]-1, cur[1]), (cur[0]-1, cur[1], 'north')))

    if(cur[2] != 'east'):
        r.append((('hor', cur[0], cur[1] - 1), (cur[0], cur[1]-1, 'west')))

    return r

def heatline(grid, r, c, dr, dc):
    v = 16
    while(r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])):
        grid[r][c] = grid[r][c] + v
        r = r + dr
        c = c + dc
        v = v/4

def getopenness(m):
    grid = [[1 for c in range(m['c_len'])] for r in range(m['r_len'])]

    for r in range(1, m['r_len']):
        for c in range(m['c_len']):
            if(m['hor'][r][c] == 1):
                heatline(grid, r, c, 1, 0)
                heatline(grid, r-1, c, -1, 0)

    for r in range(m['r_len']):
        for c in range(1, m['c_len']):
            if(m['ver'][r][c] == 1):
                heatline(grid, r, c, 0, 1)
                heatline(grid, r, c-1, 0, -1)

    return grid

def pickopt(opt, grd):
    l = []

    for op in opt:
        if(op[0][0] == 'hor'):
            l.append([grd[op[0][1]][op[0][2]] + grd[op[0][1]-1][op[0][2]], op])
        else:
            l.append([grd[op[0][1]][op[0][2]] + grd[op[0][1]][op[0][2]-1], op])

    total = sum([li[0] for li in l])

    for li in l:
        li[0] = 1 - (li[0]/total)

    l[0][0] = l[0][0]/(len(l)-1)
    for i in range(1, len(l)):
        l[i][0] = l[i][0]/(len(opt)-1) + l[i-1][0]

    r = random()
    #print(l)
    for li in l:
        if(r < li[0]):
            return li[1]
    

def randWallLayout(edges = [[standardWall(y) for y in range(30)] for x in range(4)]):
    clen = len(edges[0])
    rlen = len(edges[1])
    mindensity = 2*(clen+rlen)/(clen*rlen)

    m = {'hor': [[0 for c in range(clen)] for r in range(rlen+1)],
        'ver': [[0 for c in range(clen+1)] for r in range(rlen)],
        'space': [[8 for c in range(clen)] for r in range(rlen)],
        'r_len': rlen,
        'c_len': clen}

    for i in range(clen):
        m['hor'][0][i] = edges[0][i]
        m['hor'][rlen][i] = edges[2][i]

    for i in range(rlen):
        m['ver'][i][0] = edges[1][i]
        m['ver'][i][clen] = edges[3][i]

    reset = True
    graid = getopenness(m)
    while(getInnerDensity(m) < mindensity):
        if(reset):
            current = randstart(m)
            reset = False
        opt = getwallopt(m, current)

        if(len(opt) == 0):
            reset = True
            graid = getopenness(m)
            continue

        op = pickopt(opt, graid)
        m[op[0][0]][op[0][1]][op[0][2]] = 1
        current = op[1]

    return m

wallchar = [(' ', ' '), ('|', '-'), ('-', '\\')]

def wallprint(m, filename = 'temp.txt'):
    lines = []

    for r in range(m['r_len']):
        lines.append('+ ' + ' + '.join([wallchar[m['hor'][r][c]][1] for c in range(m['c_len'])]) + ' +\n')
        lines.append('   '.join([wallchar[m['ver'][r][c]][0] for c in range(m['c_len']+1)]) + '\n')

    lines.append('+ ' + ' + '.join([wallchar[m['hor'][m['r_len']][c]][1] for c in range(m['c_len'])]) + ' +\n')

    f = open(filename, 'w')
    f.writelines(lines)
    f.close()

wallprint(randWallLayout())
    
    
