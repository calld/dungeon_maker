from random import randrange, random, triangular
import math
from util import roll

# cash object = [cp: int, sp: int, ep: int, gp: int, pp: int]

def combineCash (o1, o2, func = lambda x, y: x+y):
    """combineCash(o1, o2, func = lambda x, y: x+y), combine two lists using func"""
    return [func(o1[x], o2[x]) for x in range(len(o1))]

def cashToString(cash):
    return '{} cp, {} sp, {} ep, {} gp, {} pp'.format(cash[0], cash[1], cash[2], cash[3], cash[4])

#roll functions for gems and art here

def getTreasure(lvl):
    """get basic treasure"""
    r = {}
    cr = randrange(1, 101) + (lvl-2)*18
    if(cr < 31):
        r['cash'] = [roll(5, 6), 0, 0, 0, 0]
    elif(cr < 61):
        r['cash'] = [0, roll(4,6), 0, 0, 0]
    elif(cr < 71):
        r['cash'] = [0, 0, roll(3, 6), 0, 0]
    elif(cr < 96):
        r['cash'] = [0,0,0,roll(3, 6),0]
    elif(cr < 101):
        r['cash'] = [0, 0, 0, 0, roll(1, 6)]
    elif(cr < 131):
        r['cash'] = [roll(4, 6)*100, 0, roll(1, 6)*10, 0, 0]
    elif(cr < 161):
        r['cash'] = [0, roll(6, 6)*10, 0, roll(2, 6)*10, 0]
    elif(cr < 171):
        r['cash'] = [0,0, roll(3, 6)*10, roll(2, 6)*10, 0]
    elif(cr < 196):
        r['cash'] = [0, 0, 0, roll(4, 6) * 10, 0]
    elif(cr < 201):
        r['cash'] = [0,0,0,roll(2, 6)*10, roll(3, 6)]
    elif(cr < 221):
        r['cash'] = [0, roll(4, 6)*100, 0, roll(1, 6)*100, 0]
    elif(cr < 236):
        r['cash'] = [0,0,roll(1, 6)*100, roll(1, 6)*100, 0]
    elif(cr < 276):
        r['cash'] = [0,0, 0, roll(2, 6)*100, roll(1, 6)*10]
    elif(cr < 301):
        r['cash'] = [0, 0, 0, roll(2, 6)*100, roll(2, 6)*10]
    elif(cr < 316):
        r['cash'] = [0, 0, roll(2, 6)*1000, roll(8, 6)*100, 0]
    elif(cr < 356):
        r['cash'] = [0, 0, 0, roll(1, 6)*1000, roll(1, 6)*100]
    else:
        r['cash'] = [0,0,0, roll(1, 6)*1000, roll(2, 6) * 100]
    return r

def getHoard(lvl):
    """get major reward"""
    r = {'cash': [],
         'loot': ''}
    cr = randrange(1, 101) + (lvl-2)*18
    if(cr < 101):
        r['cash'] = [roll(6, 6)*100, roll(3, 6)*100, 0, roll(2, 6)*10, 0]
        if(cr < 7):
            "nothin"
        elif(cr < 17):
            r['loot'] = str(roll(2, 6)) + ' 10 gp gems'
        elif(cr < 27):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects'
        elif(cr < 37):
            r['loot'] = str(roll(2, 6)) + ' 50 gp gems'
        elif(cr < 45):
            r['loot'] = str(roll(2, 6)) + ' 10 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table A)'
        elif(cr < 53):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 6)) + ' Magic Items(table A)'
        elif(cr < 61):
            r['loot'] = str(roll(2, 6)) + ' 50 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table A)'
        elif(cr < 66):
            r['loot'] = str(roll(2, 6)) + ' 10 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table B)'
        elif(cr < 71):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table B)'
        elif(cr < 76):
            r['loot'] = str(roll(2, 6)) + ' 50 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table B)'
        elif(cr < 79):
            r['loot'] = str(roll(2, 6)) + ' 10 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table C)'
        elif(cr < 81):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table C)'
        elif(cr < 86):
            r['loot'] = str(roll(2, 6)) + ' 50 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table C)'
        elif(cr < 93):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table F)'
        elif(cr < 98):
            r['loot'] = str(roll(2, 6)) + ' 50 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table F)'
        elif(cr < 100):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and one Magic Item(table G)'
        else:
            r['loot'] = str(roll(2, 6)) + ' 50 gp gems and one Magic Item(table G)'
    elif(cr < 201):
        r['cash'] = [roll(2, 6)*100, roll(2, 6)*1000, 0, roll(6, 6)*100, roll(3, 6)*10]
        cr = cr - 100
        if(cr < 5):
            "nothin"
        elif(cr < 11):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects'
        elif(cr < 17):
            r['loot'] = str(roll(3, 6)) + ' 50 gp gems'
        elif(cr < 23):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems'
        elif(cr < 29):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects'
        elif(cr < 33):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 6)) + ' Magic Items(table A)'
        elif(cr < 37):
            r['loot'] = str(roll(3, 6)) + ' 50 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table A)'
        elif(cr < 41):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table A)'
        elif(cr < 45):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 6)) + ' Magic Items(table A)'
        elif(cr < 50):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table B)'
        elif(cr < 55):
            r['loot'] = str(roll(3, 6)) + ' 50 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table B)'
        elif(cr < 60):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table B)'
        elif(cr < 64):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table B)'
        elif(cr < 67):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table C)'
        elif(cr < 70):
            r['loot'] = str(roll(3, 6)) + ' 50 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table C)'
        elif(cr < 73):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table C)'
        elif(cr < 75):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table C)'
        elif(cr < 77):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and 1 Magic Item(table D)'
        elif(cr < 79):
            r['loot'] = str(roll(3, 6)) + ' 50 gp gems and 1 Magic Item(table D)'
        elif(cr < 80):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems and 1 Magic Item(table D)'
        elif(cr < 81):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and 1 Magic Item(table D)'
        elif(cr < 85):
            r['loot'] = str(roll(2, 4)) + ' 25 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table F)'
        elif(cr < 89):
            r['loot'] = str(roll(3, 6)) + ' 50 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table F)'
        elif(cr < 92):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table F)'
        elif(cr < 95):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table F)'
        elif(cr < 97):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table G)'
        elif(cr < 99):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table G)'
        elif(cr < 100):
            r['loot'] = str(roll(3, 6)) + ' 100 gp gems and 1 Magic Item(table H)'
        else:
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and 1 Magic Item(table H)'
    elif(cr < 301):
        r['cash'] = [0,0,0, roll(4, 6)*1000, roll(5, 6)*100]
        cr = cr - 200
        if(cr < 4):
            "nothin"
        elif(cr < 7):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects'
        elif(cr < 11):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects'
        elif(cr < 13):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems'
        elif(cr < 16):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems'
        elif(cr < 20):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects, ' + str(roll(1, 4)) + ' Magic Items(table A) and ' + str(roll(1, 6)) + ' Magic Items(table B)'
        elif(cr < 24):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects, ' + str(roll(1, 4)) + ' Magic Items(table A) and ' + str(roll(1, 6)) + ' Magic Items(table B)'
        elif(cr < 27):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems, ' + str(roll(1, 4)) + ' Magic Items(table A) and ' + str(roll(1, 6)) + ' Magic Items(table B)'
        elif(cr < 30):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems, ' + str(roll(1, 4)) + ' Magic Items(table A) and ' + str(roll(1, 6)) + ' Magic Items(table B)'
        elif(cr < 36):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 6)) + ' Magic Ttems(table C)'
        elif(cr < 41):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects and ' + str(roll(1, 6)) + ' Magic Ttems(table C)'
        elif(cr < 46):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems and ' + str(roll(1, 6)) + ' Magic Ttems(table C)'
        elif(cr < 51):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 6)) + ' Magic Ttems(table C)'
        elif(cr < 55):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table D)'
        elif(cr < 59):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects and ' + str(roll(1, 4)) + ' Magic Ttems(table D)'
        elif(cr < 63):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems and ' + str(roll(1, 4)) + ' Magic Ttems(table D)'
        elif(cr < 67):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 4)) + ' Magic Ttems(table D)'
        elif(cr < 69):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and 1 Magic Item(table E)'
        elif(cr < 71):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects and 1 Magic Item(table E)'
        elif(cr < 73):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems and 1 Magic Item(table E)'
        elif(cr < 75):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and 1 Magic Item(table E)'
        elif(cr < 77):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects, 1 Magic Item(table F) and ' + str(roll(1, 4)) + ' Magic Item(table G)'
        elif(cr < 79):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects, 1 Magic Item(table F) and ' + str(roll(1, 4)) + ' Magic Item(table G)'
        elif(cr < 81):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems, 1 Magic Item(table F) and ' + str(roll(1, 4)) + ' Magic Item(table G)'
        elif(cr < 83):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems, 1 Magic Item(table F) and ' + str(roll(1, 4)) + ' Magic Item(table G)'
        elif(cr < 86):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table H)'
        elif(cr < 89):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects and ' + str(roll(1, 4)) + ' Magic Ttems(table H)'
        elif(cr < 91):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems and ' + str(roll(1, 4)) + ' Magic Ttems(table H)'
        elif(cr < 93):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 4)) + ' Magic Ttems(table H)'
        elif(cr < 95):
            r['loot'] = str(roll(2, 4)) + ' 250 gp art objects and 1 Magic Item(table I)'
        elif(cr < 97):
            r['loot'] = str(roll(2, 4)) + ' 750 gp art objects and 1 Magic Item(table I)'
        elif(cr < 99):
            r['loot'] = str(roll(3, 6)) + ' 500 gp gems and 1 Magic Item(table I)'
        else:
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and 1 Magic Item(table I)'
    else:
        r['cash'] = [0, 0, 0, roll(12, 6)*1000, roll(8, 6)*1000]
        cr = cr - 300
        if(cr < 3):
            "nothin"
        elif(cr < 6):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 8)) + ' Magic Items(table C)'
        elif(cr < 9):
            r['loot'] = str(roll(1, 10)) + ' 2500 gp art objects and ' + str(roll(1, 8)) + ' Magic Items(table C)'
        elif(cr < 12):
            r['loot'] = str(roll(1, 4)) + ' 7500 gp art objects and ' + str(roll(1, 8)) + ' Magic Items(table C)'
        elif(cr < 15):
            r['loot'] = str(roll(1, 8)) + ' 5000 gp gems and ' + str(roll(1, 8)) + ' Magic Items(table C)'
        elif(cr < 23):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table D)'
        elif(cr < 31):
            r['loot'] = str(roll(1, 10)) + ' 2500 gp art objects and ' + str(roll(1, 6)) + ' Magic Items(table D)'
        elif(cr < 39):
            r['loot'] = str(roll(1, 4)) + ' 7500 gp art objects and ' + str(roll(1, 6)) + ' Magic Items(table D)'
        elif(cr < 47):
            r['loot'] = str(roll(1, 8)) + ' 5000 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table D)'
        elif(cr < 53):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table E)'
        elif(cr < 59):
            r['loot'] = str(roll(1, 10)) + ' 2500 gp art objects and ' + str(roll(1, 6)) + ' Magic Items(table E)'
        elif(cr < 64):
            r['loot'] = str(roll(1, 4)) + ' 7500 gp art objects and ' + str(roll(1, 6)) + ' Magic Items(table E)'
        elif(cr < 69):
            r['loot'] = str(roll(1, 8)) + ' 5000 gp gems and ' + str(roll(1, 6)) + ' Magic Items(table E)'
        elif(cr < 70):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table G)'
        elif(cr < 71):
            r['loot'] = str(roll(1, 10)) + ' 2500 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table G)'
        elif(cr < 72):
            r['loot'] = str(roll(1, 4)) + ' 7500 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table G)'
        elif(cr < 73):
            r['loot'] = str(roll(1, 8)) + ' 5000 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table G)'
        elif(cr < 75):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table H)'
        elif(cr < 77):
            r['loot'] = str(roll(1, 10)) + ' 2500 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table H)'
        elif(cr < 79):
            r['loot'] = str(roll(1, 4)) + ' 7500 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table H)'
        elif(cr < 81):
            r['loot'] = str(roll(1, 8)) + ' 5000 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table H)'
        elif(cr < 86):
            r['loot'] = str(roll(3, 6)) + ' 1000 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table I)'
        elif(cr < 91):
            r['loot'] = str(roll(1, 10)) + ' 2500 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table I)'
        elif(cr < 96):
            r['loot'] = str(roll(1, 4)) + ' 7500 gp art objects and ' + str(roll(1, 4)) + ' Magic Items(table I)'
        else:
            r['loot'] = str(roll(1, 8)) + ' 5000 gp gems and ' + str(roll(1, 4)) + ' Magic Items(table I)'

    return r
