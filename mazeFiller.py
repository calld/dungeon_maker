from random import randrange, random
from util import randdiff
import encounter
import personality

file = open('monster_list.txt', 'r')
temp = []
for line in file:
    temp.append(line[:-1].split(', '))

monsters = {0: temp[0],
             1/8: temp[1],
             1/4: temp[2],
             1/2: temp[3],
             1: temp[4],
             2: temp[5],
             3: temp[6],
             4: temp[7],
             5: temp[8],
             6: temp[9],
             7: temp[10],
             8: temp[11],
             9: temp[12],
             10: temp[13],
             11: temp[14],
             12: temp[15],
             13: temp[16],
             14: temp[17],
             15: temp[18],
             16: temp[19],
             17: temp[20],
             18: temp[21],
             19: temp[22],
             20: temp[23],
             21: temp[24],
             22: temp[25],
             23: temp[26],
             24: temp[27],
            25: [''],
            26: [''],
            27: [''],
            28: [''],
            29: [''],
            30: ['']}

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
