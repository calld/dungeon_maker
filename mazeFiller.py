from random import randrange

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
             24: temp[27]}

def randMonster(cr):
    return monsters[cr][randrange(0, len(monsters[cr]))]
