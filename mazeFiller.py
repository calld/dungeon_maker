from random import randrange, random
from util import randdiff
import encounter
import personality

monsters = {}

def initMonsters(fn = 'Ref/monster_list.txt', mon = monsters):
    f = open(fn, 'r')
    lines = [line.split(', ') for line in f]
    f.close()
    for x in range(1, 25):
        mon[x] = lines[x+3]
    for x in range(25, 31):
        mon[x] = ['']
    mon[0] = lines[0]
    mon[1/8] = lines[1]
    mon[1/4] = lines[2]
    mon[1/2] = lines[3]
				
initMonsters()
#print(monsters)

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
