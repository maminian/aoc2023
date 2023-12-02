import csv

with open('input', 'r') as f:
    lines = list( csv.reader(f, delimiter=':') )

games = [[li.strip() for li in l[1].split(';')] for l in lines]

caps = {'red': 12, 'green': 13, 'blue': 14}

def check_valid(game, caps=caps):
    for round in game:
        doi = round.split(',')
        for d in doi:
            d = d.strip()
            n,color = d.split(' ')
            if color not in caps.keys():
                return False
            if caps[color] < int(n):
                return False
    return True

valids = [check_valid(g) for g in games]

c = 0
for i in range(len(valids)):
    if valids[i]:
        c += i+1 # games start at 1, not 0
print(c)

##########

def get_min_viable(game):
    mins = {}
    for round in game:
        doi = round.split(',')
        for d in doi:
            d = d.strip()
            n,color = d.split(' ')
            if color not in mins.keys():
                mins[color] = int(n)
            else:
                mins[color] = max(mins[color], int(n))
    return mins

def dicepower(dset):
    if any([col not in dset.keys() for col in ['red', 'blue', 'green']]):
        return 0
    return dset['red']*dset['blue']*dset['green']

powers = [dicepower(get_min_viable(g)) for g in games]
print(sum(powers))

