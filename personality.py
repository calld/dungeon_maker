from random import random, randrange, triangular
from util import randdiff
import math

MBstat = {
    'ISTJ' : {
        'desc' : """Quiet, serious, earn success by thoroughness and dependability. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized - their work, their home, their life. Value traditions and loyalty.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'ISTP' : {
        'desc' : """Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'ESTP' : {
        'desc' : """Flexible and tolerant, they take a pragmatic approach focused on immediate results. Theories and conceptual explanations bore them - they want to act energetically to solve the problem. Focus on the here-and-now, spontaneous, enjoy each moment that they can be active with others. Enjoy material comforts and style. Learn best through doing.""",
        'align': ['NN', 'NG', 'CN', 'CG']
        },
    'ESTJ' : {
        'desc' : """Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'ISFJ' : {
        'desc' : """Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'ISFP' : {
        'desc' : """Quiet, friendly, sensitive, and kind. Enjoy the present moment, what's going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts, do not force their opinions or values on others.""",
        'align': ['NN', 'NG', 'CN', 'CG']
        },
    'ESFP' : {
        'desc' : """Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work, and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people.""",
        'align': ['NN', 'NG', 'CN', 'CG']
        },
    'ESFJ' : {
        'desc' : """Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-by-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'INFJ' : {
        'desc' : """Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision.""",
        'align': ['LG', 'NG', 'CG']
        },
    'INFP' : {
        'desc' : """Idealistic, loyal to their values and to people who are important to them. Want an external life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'ENFP' : {
        'desc' : """Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency.""",
        'align': ['NN', 'NG', 'CN', 'CG']
        },
    'ENFJ' : {
        'desc' : """Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership.""",
        'align': ['NN', 'NG', 'CN', 'CG']
        },
    'INTJ' : {
        'desc' : """Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance - for themselves and others.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'INTP' : {
        'desc' : """Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical.""",
        'align': ['NN','LN', 'LG', 'NG']
        },
    'ENTP' : {
        'desc' : """Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another.""",
        'align': ['NN', 'NG', 'CN', 'CG']
        },
    'ENTJ' : {
        'desc' : """Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas.""",
        'align': ['NN','LN', 'LG', 'NG']
        }
    }

MBtable = [(.116, 'ISTJ'),
           (.17,  'ISTP'),
           (.213, 'ESTP'),
           (.3,   'ESTJ'),
           (.437, 'ISFJ'),
           (.524, 'ISFP'),
           (.609, 'ESFP'),
           (.731, 'ESFJ'),
           (.746, 'INFJ'),
           (.79,  'INFP'),
           (.871, 'ENFP'),
           (.896, 'ENFJ'),
           (.917, 'INTJ'),
           (.95,  'INTP'),
           (.982, 'ENTP'),
           (1,    'ENTJ')]

def formatParagraph(string, jump = 60):
    s = string
    i = jump
    while(i < len(s)):
        if(s[i] == ' '):
            s = s[:i] + '\n' + s[i+1:]
            i = i + jump
        else:
            i = i + 1

    return s

def randPersonality():
    r = random()
    for i in range(len(MBtable)):
        if(r < MBtable[i][0]):
            return {'type': MBtable[i][1],
                    'desc': MBstat[MBtable[i][1]]['desc'],
                    'align': MBstat[MBtable[i][1]]['align'][randrange(0, len(MBstat[MBtable[i][1]]['align']))]}
    return {}

def randPersonEcounter(lvl):
    state = ""
    rand = random()
    if(rand < (0.24 + lvl*0.01)):
        state = "restrained"
    elif(rand < 0.57):
        state = "lost"
    elif(rand < (0.58 + lvl*0.015)):
        state = "cursed"
    else:
        state = "resting"

    typ = ""
    rand= random()
    if(rand < 0.3):
        typ = ["druid", "knight", "mage", "priest", "scout", "minstrel"][randrange(6)]
    elif(rand < .75):
        typ = "commoner"
        lvl = 1
    elif(rand < .95):
        typ = "merchant"
        if(lvl > 2):
            lvl = lvl - 2
        else:
            lvl = 1 
    else:
        typ = "royal"
        lvl = lvl - 1

    sex, pronoun = [('male', 'he'),('female', 'she')][randrange(2)]

    diff = randdiff(lvl)

    racei = math.floor(triangular(0, 8.9999, 0))
    race = ['Human', "Halfling", "Dwarf", 'Elf', "Gnome", "Dragonborn", "Half-Elf", "Half-Orc", "Tiefling"][racei]

    common = 'speaks'
    if(racei > 1 and random() < .1):
        common = "doesn't speak"

    bad = "isn't"
    if(random() < .1):
        bad = "is"

    per = randPersonality()

    return formatParagraph("Encounter: {1} {2} who {3} common, DC {4}, this {5} is currently {6}. alignment: {10}. {7} {8} evil. {7} is {9}".format('', sex, race, common, diff, typ, state, pronoun, bad, per['desc'], per['align']))
