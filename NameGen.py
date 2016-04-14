from random import randrange

def getNameLines(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    for x in range(len(lines)):
        lines[x] = lines[x].split(',')[:-1]
    return lines

def StandardName(gender, file):
    """gender = True = male, False = female"""
    lines = getNameLines(file)
    male = lines[0]
    female = lines[1]
    last = lines[2]

    if(gender):
        return '{}{}'.format(male[randrange(len(male))][1:], last[randrange(len(last))])
    else:
        return '{}{}'.format(female[randrange(len(female))][1:], last[randrange(len(last))])

def DwarfName(gender):
    """gender -> True = male, False = female"""
    return StandardName(gender, 'DwarfNames.txt')

def ElfName(gender):
    return StandardName(gender, 'ElvenNames.txt')

def HalflingName(gender):
    return StandardName(gender, 'HalflingNames.txt')

def HumanName(gender):
    return StandardName(gender, 'HumanNames.txt')

def DragonbornName(gender):
    lines = getNameLines('DragonbornNames.txt')

    if(gender):
        return '{}{}'.format(lines[2][randrange(len(lines[2]))][1:], lines[0][randrange(len(lines[0]))])
    else:
        return '{}{}'.format(lines[2][randrange(len(lines[2]))][1:], lines[1][randrange(len(lines[1]))])

def GnomeName(gender):
    lines = getNameLines('GnomeNames.txt')

    if(gender):
        return '{}{}{}'.format(lines[0][randrange(len(lines[0]))][1:], lines[3][randrange(len(lines[3]))], lines[2][randrange(len(lines[2]))])
    else:
        return '{}{}{}'.format(lines[1][randrange(len(lines[1]))][1:], lines[3][randrange(len(lines[3]))], lines[2][randrange(len(lines[2]))])

def OrcName(gender):
    orc = getNameLines('GnomeNames.txt')
    human = getNameLines('HumanNames.txt')

    if(gender):
        return '{}{}'.format(orc[0][randrange(len(orc[0]))][1:], human[2][randrange(len(human[2]))])
    else:
        return '{}{}'.format(orc[1][randrange(len(orc[1]))][1:], human[2][randrange(len(human[2]))])

def TieflingName(gender):
    lines = getNameLines('TieflingNames.txt')
    male = lines[0] + lines[2]
    female = lines[0] + lines[2]

    if(gender):
        return male[randrange(len(male))][1:]
    else:
        return female[randrange(len(female))][1:]

    
