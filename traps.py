# random trap
from util import randdiff
from random import random, randrange




#types: pits, spikes, arrows,

def randspell(lvl):
    spellfile = open('attackspells.txt', 'r')
    lines = spellfile.readlines()
    spellfile.close()
    spells = [line.split(',') for line in lines]
    splvl = lvl//2 + lvl%2
    if(splvl > 9):
        splvl = 9
    temp = spells[randrange(1, splvl+1)]
    return temp[randrange(len(temp))]
        

def randtrap(lvl):
    tt = randrange(6)
    trigger = '{}, detection: {}.'.format(['moving through it(example: wire)', 'standing on it(example: pressure plate)', 'nearby interaction (example: picking up coins)'][randrange(3)], randdiff(lvl))

    if(tt == 0):
        effect = '{0} ft x {0} ft pit opens, depth {1} ft(size bounded by walls).'.format(randrange(5, 16, 5), randrange(10, 21))

        return 'pit: triggered by {}\nwhere {}'.format(trigger, effect)

    elif(tt == 1):
        effect = '{0} ft x {0} ft pit opens, depth {1} ft(size bounded by walls). after which the top is closed, escape: {2}.'.format(randrange(5, 16, 5), randrange(10, 21), randdiff(lvl))

        disarm = 'The trap is disarmed by some kind of switch (hidden: {}), or via theives tools {}.'.format(randdiff(lvl), randdiff(lvl))

        return 'locking pit: triggered by {}\nwhere {}\n{}'.format(trigger, effect, disarm)

    elif(tt == 2):
        effect = 'spikes shoot from {0}, in {1} ft x {1} ft area (bounded by walls) all creatures within spikes make dex save {2}, dealing {3}d{4} (min 1) piercing dmg on failure.'.format(['the cieling', 'the walls', 'the floor'][randrange(3)],
                                                                                                                                                                                   randrange(5, 16, 5), randdiff(lvl),
                                                                                                                                                                                   randrange(lvl-1, lvl+2), randrange(4, 9, 2))
        disarm = 'The trap is disarmed by some kind of switch (hidden: {}), or via theives tools {}.'.format(randdiff(lvl), randdiff(lvl))

        return 'spikes: triggered by {}\nwhere {}\n{}'.format(trigger, effect, disarm)

    elif(tt == 3):
        splvl = lvl//2 + lvl%2
        if(splvl > 9):
            splvl = 9
        effect = '{} is cast at lvl {} targeting R from the {}, save = {}, attack mod = {}.'.format(randspell(lvl), splvl, ['north', 'south', 'east', 'west'][randrange(4)], randdiff(lvl), randdiff(lvl) - 8)

        disarm = 'spell can be undone with arcana(int) check DC {}, or dispel magic DC {}.'.format(randdiff(lvl), 10 + splvl)

        return 'spell trap: triggered by {}\nwhere {}\n{}'.format(trigger, effect, disarm)

    elif(tt == 4):
        effect = 'darts shoot from nearby holes, creatures within a {0} ft by {0} ft area (bounded by walls) make a dex save DC {1}; failure deals 1 piercing dmg and make a con save DC {2}, else take {3}d{4} poison dmg.'.format(randrange(5, 16, 5), randdiff(lvl),
                                                                                                                                                                                                                                   randdiff(lvl), randrange(lvl-1, lvl+2), randrange(4, 9, 2))
        disarm = 'The trap is disarmed by some kind of switch (hidden: {}), or via theives tools {}.'.format(randdiff(lvl), randdiff(lvl))

        return 'darts: triggered by {}\nwhere {}\n{}'.format(trigger, effect, disarm)
    else:
        t = randrange(5)
        if(t == 0):
            return 'Flooding: triggered by {}\nthe room begins to fill with water, d12 inches per round, the ceiling is {} ft high.\ntrap ended by correctly solving a riddle. have players roll initiative, trap has initative of 10.\nEach player gets to make 1 + int modifier guesses (min 1) on their turn'.format(trigger, randrange(7, 11))
        elif(t == 1):
            return 'Burning trap: triggered by {}\nthe room begins to heat up, all creatures in the room take Xd6 fire dmg every other round\nwhere X starts at 0 and increases by 1 each time you roll for damage (the first roll is 0d6 ie no damage).\ntrap ended by correctly solving a riddle. have players roll initiative, trap has initative of 10, each player gets to make 1 + int modifier guesses (min 1) on their turn'.format(trigger)
        elif(t == 2):
            return 'Freezing trap: triggered by {}\nthe room begins to freeze, all creatures in the room take Xd4 cold dmg every other round and is slowed by 10ft,\nwhere X starts at 0 and increases by 1 each time you roll for damage (the first roll is 0d4 ie no damage).\ntrap ended by correctly solving a riddle. have players roll initiative, trap has initative of 10, each player gets to make 1 + int modifier guesses (min 1) on their turn'.format(trigger)
        elif(t == 3):
            return 'Poison trap: triggered by {}\nthe room begins to fill with poison gas, all creatures in the room make a con save of {} taking d8 poison dmg on failure every round,\nthe trap is disarmed by some kind of switch (hidden {})'.format(trigger, randdiff(lvl), randdiff(lvl))
        else:
            return "Lightning floor: triggered by {}\nthe floor of the room becomes electrified, all creatures in the room each turn make a strength save DC {},\nfailure take 1d4 lightning dmg and be stunned till the trap's next turn,\nhave players roll initiative, trap has initative of 10. the trap is disarmed by some kind of switch (hidden {})".format(trigger, randdiff(lvl), randdiff(lvl))
        
