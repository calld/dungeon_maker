from random import randrange, random
from util import randdiff
import encounter
import personality

def initMonsters(fn = 'Ref/monster_list.txt'){
    f = open(fn, 'r')
    lines = [line.split(', ') in line in f]
    f.close()
    monsters = {0: lines[0],
                 1/8: lines[1],
                 1/4: lines[2],
                 1/2: lines[3],
                 1: lines[4],
                 2: lines[5],
                 3: lines[6],
                 4: lines[7],
                 5: lines[8],
                 6: lines[9],
                 7: lines[10],
                 8: lines[11],
                 9: lines[12],
                 10: lines[13],
                 11: lines[14],
                 12: lines[15],
                 13: lines[16],
                 14: lines[17],
                 15: lines[18],
                 16: lines[19],
                 17: lines[20],
                 18: lines[21],
                 19: lines[22],
                 20: lines[23],
                 21: lines[24],
                 22: lines[25],
                 23: lines[26],
                 24: lines[27],
                25: [''],
                26: [''],
                27: [''],
                28: [''],
                29: [''],
                30: ['']}

}

def randMonster(cr):
    return monsters[cr][randrange(0, len(monsters[cr]))]

def randDoor(lvl):
    door = {}
    if(random() < (.1 + .01*lvl)):
        door['lock'] = randdiff(lvl)
    door['strength'] = randdiff(lvl) + 5
    return door

def randSDoor(lvl):
    door = randDoor(lvl)
    door['hidden'] = randdiff(lvl)
    return door

def get_encounter(lvl, num = 4, diff = 1):
    """ get_encounter(lvl, num = 4, diff = 1): lvl = players' level, num = number of players, diff = (0 = easy, 1 = medium, 2 = hard)"""
    temp = encounter.randomEncounter(lvl, player_count = num, diff = diff)
    return (randMonster(temp[0]), temp[1])

initMonsters()


"""lvl = 12

for d in range(3):
    print(['\teasy e', '\tmedium M', '\thard H'][d])
    for i in range(1, 13):
        e = get_encounter(lvl, diff = d)
        print('{}: {}, {}'.format(i, e[0], e[1]))
    print()

print('\tdoors')
for i in range(1, 13):
    door = randDoor(lvl)
    print('{}: '.format(i), end = '')
    for k, v in door.items():
        print('{} {},'.format(k, v), end = '')
    print()
print()"""

"""print('\tpersonality')
for i in range(1, 21):
    p = personality.randPersonality()
    print('{}: type: {} alignment: {}'.format(i, p['type'], p['align']))
    print(personality.formatParagraph(p['desc']))
print()"""
