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

def eval_winners_p1(T, hiscore):
    '''
    Return number of strategies beating hiscore
    (strictly beating...?)
    Outputs integer.
    '''
    return sum([eval_hold(i,T)>hiscore for i in range(T+1)])

# part 1
p=1
for Ti,hi in zip(*data):
    p *= eval_winners_p1(Ti,hi)

print('part 1:', p)

#########
# part 2 - join numbers and re-evaluate...
import time

T = int(''.join([str(tt) for tt in data[0]]))
hiscore = int(''.join([str(tt) for tt in data[1]]))

t0 = time.time()
wow = eval_winners_p1(T,hiscore)
t1 = time.time()

print('part 2:', wow)
print('eval time: %.1f sec'%(t1-t0))
