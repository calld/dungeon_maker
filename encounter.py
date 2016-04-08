import random
import math
xpThreshold = ((25, 50, 75, 100),
             (50, 100, 150, 200),
             (75, 150, 225, 400),
             (125, 250, 375, 500),
             (250, 500, 750, 1100),
             (300, 600, 900, 1400),
             (350, 750, 1100, 1700),
             (450, 900, 1400, 2100),
             (550, 1100, 1600, 2400),
               (600, 1200, 1900, 2800),
               (800, 1600, 2400, 3600),
               (1000, 2000, 3000, 4500),
               (1100, 2200, 3400, 5100),
               (1250, 2500, 3800, 5700),
               (1400, 2800, 4300, 6400),
               (1600, 3200, 4800, 7200),
               (2000, 3900, 5900, 8800),
               (2100, 4200, 6300, 9500),
               (2400, 4900, 7300, 10900),
               (2800, 5700, 8500, 12700))

numberMult = [0, 1, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]

crxp = {0: 10,
        1/8: 25,
        1/4: 50,
        1/2: 100,
        1: 200,
        2: 450,
        3: 700,
        4: 1100,
        5: 1800,
        6: 2300,
        7: 2900,
        8: 3900,
        9: 5000,
        10: 5900,
        11: 7200,
        12: 8400,
        13: 10000,
        14: 11500,
        15: 13000,
        16: 15000,
        17: 18000,
        18: 20000,
        19: 22000,
        20: 25000,
        21: 33000,
        22: 41000,
        23: 50000,
        24: 62000,
        25: 75000,
        26: 90000,
        27: 105000,
        28: 120000,
        29: 135000,
        30: 155000}

cr = [0, 1/8, 1/4, 1/2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def get_cr_list(lvl, player_count = 4, diff = 1):
    """get_cr_list(lvl, player_count = 4, diff = 1) -> list of (cr, number) for allowed monster groups
        -lvl: level of players
        -player_count: number of players, default 4
        -diff: difficulty, 0 = easy, 1 = medium(default), 2 = hard"""
    thr = (xpThreshold[lvl - 1][diff]*player_count, xpThreshold[lvl - 1][diff+1]*player_count)
    result = []    
    for cr, xp in crxp.items():
        for x in range(player_count+2, 0, -1):
            total = xp*x*numberMult[x]
            if(total < thr[1]):
                if(total >= thr[0]):
                    result.append((cr, x))
                break;
    result.sort(key = lambda x: x[0], reverse = True)
    return result

def randomEncounter(lvl, player_count = 4, diff = 1):
    options = get_cr_list(lvl, player_count, diff)
    #options.append((0,0))
    return options[math.floor(random.triangular(0,len(options),0))]

print(get_cr_list(1, player_count = 3, diff = 2))
"""for x in range(25):
    print(randomEncounter(3, diff = 1))"""
