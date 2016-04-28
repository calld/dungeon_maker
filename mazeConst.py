import mazeGen as mg
import mazeFiller as mf
import treasure as trsr
import pickle
import os
from random import randrange
from util import randdiff
from personality import randPersonEcounter
import traps

def spaceInfo(lvl, state, string, player_count):
    if(state == 4):
        hrd = trsr.getHoard(lvl)
        return trsr.cashToString(hrd['cash']) + ' and ' + hrd['loot']
    elif(state == 5):
        return "stairs down"
    elif(state == 6):
        return "stairs up"
    elif(state == 7):
        return trsr.cashToString(trsr.getTreasure(lvl)['cash']) + ', hidden(no monster encounter): {}, Clue to {}: ({}, {})'.format(randdiff(lvl), ['goal', 'treasure1', 'treasure2'][randrange(3)], randdiff(lvl),
                                                                                                                                    ['Arcana', 'History', 'Investigation', 'Nature', 'Religion'][randrange(5)])
    elif(state == 9):
        e = mf.get_encounter(lvl, num = player_count)
        return '{} {}'.format(e[1], e[0])
    elif(state == 10):
        e = mf.get_encounter(lvl, diff = 0, num = player_count)
        return '{} {}'.format(e[1], e[0])
    elif(state == 11):
        e = mf.get_encounter(lvl, diff = 2, num = player_count)
        return '{} {}'.format(e[1], e[0])
    elif(state == 12):
        return randPersonEcounter(lvl)
    elif(state == 13):
        return traps.randtrap(lvl)
    else:
        return string

def edgeInfo(lvl, state, string):
    if(state == 2):
        s = 'door: '
        door = mf.randDoor(lvl)
        if('lock' in door):
            s = s + 'locked: {}, '.format(door['lock'])
        s = s + 'strength: {}'.format(door['strength'])
        return s
    if(state == 3):
        s = 'door: '
        door = mf.randSDoor(lvl)
        if('lock' in door):
            s = s + 'locked: {}, '.format(door['lock'])
        if('hidden' in door):
            s = s + 'hidden: {}, '.format(door['hidden'])
        s = s + 'strength: {}'.format(door['strength'])
        return s
    else:
        return string

#need to mark secret doors as spectial

def genInfo(lvl, mp, pc, moninit):
    mf.initMonsters(fn = moninit)
    s = 'floor lvl ' + str(lvl)
    return {'space': [[spaceInfo(lvl, mp['space'][r][c], s, pc) for c in range(mp['c_len'])] for r in range(mp['r_len'])],
            'hor': [[edgeInfo(lvl, mp['hor'][r][c], s) for c in range(mp['c_len'])] for r in range(mp['r_len']+1)],
            'ver': [[edgeInfo(lvl, mp['ver'][r][c], s) for c in range(mp['c_len']+1)] for r in range(mp['r_len'])]}

def makeDun(strength = [x for x in range(1, 21)], size = [(2, 2)]*4 + [(3, 3)]*7 + [(4, 4)]*5 + [(5,5)]*4, pc = 4, monsterlistfilename = "Ref/monster_list.txt", layoutType = 'maze'):
    dun = {'floor': [mg.make_floor(x[0], x[1], layoutType) for x in size]}
    dun['desc'] = 'dungeon'
    dun['info'] = [genInfo(strength[x], dun['floor'][x], pc, monsterlistfilename) for x in range(len(strength))]
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

ch = [(' ', ' '), ('|', '-'), ('-', '\\'),
      ('S','S'), 'T', 'G', 'E', 't', ' ', 'm', 'e', 'h', 'P', 'R']

ch2 = [(' ',' '), ('|', '-'), ('-', '\\'), ('|', '-')]

def make_txt(dun, name = './temp'):
    d = os.path.dirname(name)
    if (not os.path.exists(d)):
        print('making dir')
        os.makedirs(name)
    cwd = os.getcwd()
    os.chdir(name)

    save(dun, name = "Full.dun")

    for floor in range(len(dun['floor'])):
        lines = ['   ' + ''.join(['+{:0>3X}'.format(c) for c in range(dun['floor'][floor]['c_len'])]) + '+\n']

        for r in range(dun['floor'][floor]['r_len']):
            lines.append('{:0>3X}'.format(r))
            for c in range(dun['floor'][floor]['c_len']):
                lines[-1] = lines[-1] + '+ {} '.format(ch[dun['floor'][floor]['hor'][r][c]][1])
            lines[-1] = lines[-1] + '+{:0>3X}\n'.format(r)
            lines.append('{:0>3X}'.format(r))
            for c in range(dun['floor'][floor]['c_len']):
                lines[-1] = lines[-1] + '{} {} '.format(ch[dun['floor'][floor]['ver'][r][c]][0], ch[dun['floor'][floor]['space'][r][c]])
            lines[-1] = lines[-1] + ch[dun['floor'][floor]['ver'][r][dun['floor'][floor]['c_len']]][0] + '{:0>3X}\n'.format(r)

        lines.append('{:0>3X}'.format(dun['floor'][floor]['r_len']))
        for c in range(dun['floor'][floor]['c_len']):
            lines[-1] = lines[-1] + '+ {} '.format(ch[dun['floor'][floor]['hor'][dun['floor'][floor]['r_len']][c]][1])
        lines[-1] = lines[-1] + '+{:0>3X}\n'.format(dun['floor'][floor]['r_len'])

        lines.append('   ' + ''.join(['+{:0>3X}'.format(c) for c in range(dun['floor'][floor]['c_len'])]) + '+\n')

        dmap = open('Floor{:0>2d}Map.txt'.format(floor+1), 'w')
        dmap.writelines(lines)
        dmap.close()

        lines = []

        for r in range(dun['floor'][floor]['r_len']):
            for c in range(dun['floor'][floor]['c_len']):
                if(dun['floor'][floor]['space'][r][c] != 8):
                    lines.append('({:2X}, {:2X}) : {}\n'.format(r, c, dun['info'][floor]['space'][r][c]))

        mref = open('Floor{:0>2d}MonRef.txt'.format(floor+1), 'w')
        mref.writelines(lines)
        mref.close()

        lines = ['horizontal                                                   vertical\n']

        for r in range(dun['floor'][floor]['r_len'] + 1):
            for c in range(dun['floor'][floor]['c_len']):
                if(dun['floor'][floor]['hor'][r][c] > 1):
                    lines.append('({:2X}, {:2X}) : {}\n'.format(r, c, dun['info'][floor]['hor'][r][c]))


        lines2 = []

        for r in range(dun['floor'][floor]['r_len']):
            for c in range(dun['floor'][floor]['c_len'] + 1):
                if(dun['floor'][floor]['ver'][r][c] > 1):
                    lines2.append('({:2X}, {:2X}) : {}\n'.format(r, c, dun['info'][floor]['ver'][r][c]))

        for i in range(1, len(lines)):
            if(i >= len(lines2)):
                break
            spacesize = len(lines[0][:-9]) - len(lines[i])
            temp = ' '*spacesize + lines2[i]
            lines[i] = '{}{}'.format(lines[i][:-1], temp)

        dref = open('Floor{:0>2d}DoorRef.txt'.format(floor+1), 'w')
        dref.writelines(lines)
        dref.close()

        pref = open('Floor{:0>2d}PrintMap.txt'.format(floor+1), 'w')
        lines = []
        for majorC in range(dun['floor'][floor]['c_len']//30):
            for majorR in range(dun['floor'][floor]['r_len']//30):
                lines.append('   ' + ''.join(['+{:0>3X}'.format(c) for c in range(majorC*30, (majorC+1)*30)]) + '+\n')
                for r in range(majorR*30, (majorR+1)*30):
                    lines.append('{:0>3X}+'.format(r) + '+'.join([' {} '.format(ch[dun['floor'][floor]['hor'][r][c]][1]) for c in range(majorC*30, (majorC+1)*30)]) + '+{:0>3X}\n'.format(r))
                    lines.append('{:0>3X}'.format(r) + ''.join(['{} {} '.format(ch[dun['floor'][floor]['ver'][r][c]][0], ch[dun['floor'][floor]['space'][r][c]]) for c in range(majorC*30, (majorC+1)*30)]) + '{}{:0>3X}\n'.format(ch[dun['floor'][floor]['ver'][r][(majorC+1)*30]][0],r))
                lines.append('{:0>3X}+'.format((majorR+1)*30) + '+'.join([' {} '.format(ch[dun['floor'][floor]['hor'][(majorR+1)*30][c]][1]) for c in range(majorC*30, (majorC+1)*30)]) + '+{:0>3X}\n'.format((majorR+1)*30))
                lines.append('   ' + ''.join(['+{:0>3X}'.format(c) for c in range(majorC*30, (majorC+1)*30)]) + '+\n')
                lines.append('\n\n')

                pref.writelines(lines)
                lines = []

        pref.close()

        pref = open('Floor{:0>2d}PlayerMap.txt'.format(floor+1), 'w')
        lines = []
        for majorC in range(dun['floor'][floor]['c_len']//30):
            for majorR in range(dun['floor'][floor]['r_len']//30):
                lines.append('   ' + ''.join(['+{:0>3X}'.format(c) for c in range(majorC*30, (majorC+1)*30)]) + '+\n')
                for r in range(majorR*30, (majorR+1)*30):
                    lines.append('{:0>3X}+'.format(r) + '+'.join([' {} '.format(ch2[dun['floor'][floor]['hor'][r][c]][1]) for c in range(majorC*30, (majorC+1)*30)]) + '+{:0>3X}\n'.format(r))
                    lines.append('{:0>3X}'.format(r) + ''.join(['{}   '.format(ch2[dun['floor'][floor]['ver'][r][c]][0]) for c in range(majorC*30, (majorC+1)*30)]) + '{}{:0>3X}\n'.format(ch[dun['floor'][floor]['ver'][r][(majorC+1)*30]][0],r))
                lines.append('{:0>3X}+'.format((majorR+1)*30) + '+'.join([' {} '.format(ch2[dun['floor'][floor]['hor'][(majorR+1)*30][c]][1]) for c in range(majorC*30, (majorC+1)*30)]) + '+{:0>3X}\n'.format((majorR+1)*30))
                lines.append('   ' + ''.join(['+{:0>3X}'.format(c) for c in range(majorC*30, (majorC+1)*30)]) + '+\n')
                lines.append('\n\n')

                pref.writelines(lines)
                lines = []

        pref.close()

    os.chdir(cwd)

make_txt(makeDun(pc = 5, monsterlistfilename = "Ref/GraceCampaignMonsters.txt", layoutType = 'cave'), name = './dungeontest')
