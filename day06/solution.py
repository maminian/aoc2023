import csv

with open('input', 'r') as f:
    # row 0: high score (distance);
    # row 1: duration of race.
    data = [ [int(li) for li in l[1].strip().split()] for l in csv.reader(f, delimiter=':')]

def eval_hold(held, T):
    '''Evaluates distance traveled 
    according to race description (each ms 
    held builds speed; travels with remaining 
    time)
    '''
    return max(T-held,0)*held

def eval_winners_v1(T, hiscore):
    '''
    Return number of strategies beating hiscore
    (strictly beating...?)
    Outputs integer.
    '''
    return sum([eval_hold(i,T)>hiscore for i in range(T+1)])

# part 1
p=1
for Ti,hi in zip(*data):
    p *= eval_winners_v1(Ti,hi)

print('part 1:', p)

#########
# part 2 - join numbers and re-evaluate...
import time

T = int(''.join([str(tt) for tt in data[0]]))
hiscore = int(''.join([str(tt) for tt in data[1]]))

t0 = time.time()
wow = eval_winners_v1(T,hiscore)
t1 = time.time()

print('part 2:', wow)
print('eval time: %.1f sec'%(t1-t0))


###
#import numpy as np
#
#
# Since the function to evaluate is 
# max(T-x,0)*x - hiscore > 0,
# (a) we're already limiting the range to 
# 0 <= x <= T, so max is unnecessary; 
# then, we want to further estimate 
# lower/upper bounds for this.
#
# (T-x)x - H = 0 implies 
# x^2 -Tx + H = 0
# implies
# x = T/2 +/- sqrt((T/2)^2 - H).
def eval_winners_v2(T,hiscore):
    import numpy as np
    discr = (T/2)**2 - hiscore
    if discr <0:
        return 0
    else:
        lo = np.ceil(T/2 - np.sqrt(discr)) # lower bound
        hi = np.floor(T/2 + np.sqrt(discr))
        count = hi-lo+1
        # eval edge cases
        count += eval_hold(lo-1,T)>hiscore + eval_hold(hi+1,T)>hiscore
        return int(count)

for Ti,hi in zip(*data):
    print('v1: %i; v2: %i'%(eval_winners_v1(Ti,hi), eval_winners_v2(Ti,hi)))

t2 = time.time()
wow2 = eval_winners_v2(T,hiscore)
t3 = time.time()

print('part 2 brute force: %i; math: %i'%(wow, wow2))
print('eval time: %.1f sec'%(t3-t2))


