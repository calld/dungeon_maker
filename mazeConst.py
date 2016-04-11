import mazeGen as mg
import mazeFiller as mf
import treasure as trsr
import pickle

def spaceInfo(lvl, state, string):
    if(state == 4):
        hrd = trsr.getHoard(lvl)
        return trsr.cashToString(hrd['cash']) + ' and ' + hrd['loot']
    elif(state == 5):
        return "stairs down"
    elif(state == 6):
        return "stairs up"
    elif(state == 7):
        return trsr.cashToString(trsr.getTreasure(lvl)['cash'])
    elif(state == 9):
        e = mf.get_encounter(lvl)
        return '{} {}'.format(e[1], e[0])
    elif(state == 10):
        e = mf.get_encounter(lvl, diff = 0)
        return '{} {}'.format(e[1], e[0])
    elif(state == 11):
        e = mf.get_encounter(lvl, diff = 2)
        return '{} {}'.format(e[1], e[0])
    else:
        return string

def edgeInfo(lvl, state, string):
    if(state == 2):
        s = 'door: '
        door = mf.randDoor(lvl)
        if('lock' in door):
            s = s + 'locked: {}, '.format(door['lock'])
        if('hidden' in door):
            s = s + 'hidden: {}, '.format(door['hidden'])
        s = s + 'strength: {}'.format(door['strength'])
        return s
    else:
        return string

def genInfo(lvl, mp):
    s = 'floor lvl ' + str(lvl)
    return {'space': [[spaceInfo(lvl, mp['space'][r][c], s) for c in range(mp['c_len'])] for r in range(mp['r_len'])],
            'hor': [[edgeInfo(lvl, mp['hor'][r][c], s) for c in range(mp['c_len'])] for r in range(mp['r_len']+1)],
            'ver': [[edgeInfo(lvl, mp['ver'][r][c], s) for c in range(mp['c_len']+1)] for r in range(mp['r_len'])]}

def makeDun(strength = [x for x in range(1, 21)], size = [(2, 2)]*4 + [(3, 3)]*7 + [(4, 4)]*5 + [(5,5)]*4):
    dun = {'floor': [mg.make_floor(x[0], x[1]) for x in size]}
    dun['desc'] = 'dungeon'
    dun['info'] = [genInfo(strength[x], dun['floor'][x]) for x in range(len(strength))]
    return dun

def save(ob, name = 'temp.psav'):
    file = open(name, mode = 'wb')
    pickle.dump(ob, file)
    file.close()

def load(name = 'temp.psav'):
    file = open(name, mode = 'rb')
    res = pickle.load(file)
    file.close()
    return res
