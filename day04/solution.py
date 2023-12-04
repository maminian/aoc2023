import csv
import numpy as np

with open('input', 'r') as f:
    cards_raw = list(csv.reader(f, delimiter=':'))
    cards_raw = [c[1].split('|') for c in cards_raw]
#    cards = [[ [int(ci) if len(ci)>0 for ci in c[0].strip().split(' ')]c[0].strip().split(' '), c[1].strip().split(' ')] for c in cards]
    cards = []
    for c in cards_raw:
        left = np.array([int(ci) for ci in c[0].strip().split(' ') if len(ci)>0])
        right = np.array([int(ci) for ci in c[1].strip().split(' ') if len(ci)>0])
        cards.append([left,right])
        
# part 1
# matches and summing
def eval_scratchy(card):
    k=1
    match = False
    for f in card[0]:
        if f in card[1]:
            k *= 2
            match = True
    return match*k//2

s = 0
for c in cards:
    mo = eval_scratchy(c)
    #print(c,mo)
    s += mo
    
print(s)

###

print('part 2...')
memo = {}
def count_scratchies(idx):
    # pass on the memoized value if we've already computed
    # it for this card ID.
    if idx in memo.keys():
        return memo[idx]

    k=0
    for f in cards[idx][0]:
        if f in cards[idx][1]:
            k += 1
    # how many *child* cards does card "idx" represent?
    first, last = idx+1, idx+k+1
#    print(idx, list(range(idx+1,last)))
    memo[idx] = k+sum([count_scratchies(j) for j in range(first,last)])

    return memo[idx]
#


count = 0
for i in range(len(cards)):
    tree_count = count_scratchies(i) 
    print('parent', i, '; count: ', tree_count+1)
    count += tree_count +1 # all children, plus the parent itself

print('total scratchies: ', count)

