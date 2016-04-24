from random import randrange, random
from randomwalls import wallprint

def makeroomgrid(grid, typecount):
    options = [x for x in range(1, typecount+1)]
    roomspots = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if(grid[r][c] == 0):
                roomspots.append((r, c))

    while(len(roomspots) > 0):
        spot = roomspots.pop(randrange(len(roomspots)))
        adj = []
        if(spot[0]-1 > -1 and grid[spot[0]-1][spot[1]] > 0):
            adj.append(grid[spot[0]-1][spot[1]])
        if(spot[0]+1 < len(grid) and grid[spot[0]+1][spot[1]] > 0):
            adj.append(grid[spot[0]+1][spot[1]])
        if(spot[1]-1 > -1 and grid[spot[0]][spot[1]-1] > 0):
            adj.append(grid[spot[0]][spot[1]-1])
        if(spot[1]+1 < len(grid[spot[0]]) and grid[spot[0]][spot[1]+1] > 0):
            adj.append(grid[spot[0]][spot[1]+1])
        if(len(adj) == 0):
            grid[spot[0]][spot[1]] = options[randrange(len(options))]
        else:
            grid[spot[0]][spot[1]] = adj[randrange(len(adj))]

def xtrcRoom(grid, r, c):
    roomid = grid[r][c]
    tempgr = [[grid[f][g] for g in range(len(grid[f]))] for f in range(len(grid))]
    roomsp = []
    nextspots = [(r, c)]
    while(len(nextspots) > 0):
        spot = nextspots.pop()
        if(tempgr[spot[0]][spot[1]] == roomid):
            roomsp.append(spot)
            tempgr[spot[0]][spot[1]] = 0
            if(spot[0]+1 < len(tempgr)):
                nextspots.append((spot[0] + 1, spot[1]))
            if(spot[0]-1 > -1):
                nextspots.append((spot[0] - 1, spot[1]))
            if(spot[1] + 1 < len(tempgr[spot[0]])):
                nextspots.append((spot[0], spot[1] + 1))
            if(spot[1] - 1 > -1):
                nextspots.append((spot[0], spot[1] - 1))
    return roomsp

def roomedges(grid, sps):
    roomid = grid[sps[0][0]][sps[0][1]]
    walls = []

    for sp in sps:
        if(sp[0] > 0 and grid[sp[0]-1][sp[1]] != roomid):
            walls.append(('hor', sp[0], sp[1]))
        if(sp[1] > 0 and grid[sp[0]][sp[1]-1] != roomid):
            walls.append(('ver', sp[0], sp[1]))
        if(sp[0]+1 < len(grid) and grid[sp[0]+1][sp[1]] != roomid):
            walls.append(('hor', sp[0]+1, sp[1]))
        if(sp[1]+1 < len(grid[sp[0]]) and grid[sp[0]][sp[1]+1] != roomid):
            walls.append(('ver', sp[0], sp[1]+1))

    return walls
    

def addroomfeatures(m, edges, spaces):
    doornum, f = divmod(len(spaces)/12, 1)
    if(random() < f):
        doornum = doornum + 1

    walls = [edge for edge in edges if lambda x: m[x[0]][x[1]][x[2]] == 1]
    for x in range(int(doornum)):
        spot = walls.pop(randrange(len(walls)))
        m[spot[0]][spot[1]][spot[2]] = 2
        if(len(walls) == 0):
            break;        

def randroomsLayout(density = 4, encounters = randrange(12, 15)):
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

    rmat = [[0 for c in range(30)] for r in range(30)]
    for x in [10, 11, 18, 19]:
        rmat[0][x] = 1
        rmat[1][x] = 1
        rmat[29][x] = 1
        rmat[28][x] = 1
        rmat[x][0] = 1
        rmat[x][1] = 1
        rmat[x][29] = 1
        rmat[x][28] = 1

    makeroomgrid(rmat, density)

    for r in range(1, 30):
        for c in range(30):
            if(rmat[r][c] != rmat[r-1][c]):
                m['hor'][r][c] = 1

    for r in range(30):
        for c in range(1, 30):
            if(rmat[r][c] != rmat[r][c-1]):
                m['ver'][r][c] = 1

    marked = [[0 for c in range(30)] for r in range(30)]
    roomlists = []
    for r in range(30):
        for c in range(30):
            if(marked[r][c] == 0):
                sps = xtrcRoom(rmat, r, c)
                for sp in sps:
                    marked[sp[0]][sp[1]] = 1
                roomlists.append(sps)

    for room in roomlists:
        addroomfeatures(m, roomedges(rmat, room), room)

    enroomc = [0 for room in roomlists]

    while(encounters > 0):
        if(len(roomlists) == 0):
            break
        i = randrange(len(roomlists))
        room = roomlists[i]
        if(len(room) < 12):
            roomlists.pop(i)
            enroomc.pop(i)
            continue
        sp = room.pop(randrange(len(room)))
        m['space'][sp[0]][sp[1]] = 9
        if(len(room) > 0):
            sp = room.pop(randrange(len(room)))
            m['space'][sp[0]][sp[1]] = 7
        encounters = encounters - 1
        enroomc[i] = enroomc[i] + 1
        if(len(room)/enroomc[i] < 64):
            roomlists.pop(i)
            enroomc.pop(i)         

    return m

wallprint(randroomsLayout())

    
