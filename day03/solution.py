import csv

with open('input', 'r') as f:
    lines = list(csv.reader(f))

numbers = []
sr = []
sc = []
# gather numbers, and their positions
for i,line in enumerate(lines):
    number = ''
    flag=False
    for j,char in enumerate(line[0]):
        if char in '0123456789':
            if not flag:
                flag=True
                l = int(j)
            number += char
        elif flag:
            numbers.append( (i,l,j, int(number)) )
            flag = False
            number = ''
        # gather non-period symbols, and their positions
        if char not in '0123456789.':
            sr.append(i)
            sc.append(j)
            if flag:
                flag = False
                numbers.append( (i,l,j, int(number)) )
        if flag and j==len(line[0])-1:
            numbers.append( (i,l,j, int(number)) )

# rearrange
sr2 = [[] for _ in range(len(lines))]
for r,c in zip(sr,sc):
    sr2[r].append(c)

# low tech: go through 
#pr = 0 # number list active row
s = 0 # sum
store = {}
for entry in numbers:
    # scan neighboring rows
    cont = False
    for k in range( max(0,entry[0]-1) , min(len(lines),entry[0]+2) ):
        # are any of the column indices in range of a symbol?
#        print(entry,k)
        for ci in sr2[k]:
            if ci >= max(0,entry[1]-1) and ci <= min(len(lines[0][0]),entry[2]): # possible +1
#                print(entry[0],k,ci,entry[1])
                s += entry[3]
                print(entry, lines[k][0][ci], k, entry[1]-1, entry[2])
                cont = True

                # related to part 2.
                if (k,ci) in store.keys():
                    store[(k,ci)]['parts'].append( entry[3] )
                else:
                    store[(k,ci)] = {'symbol':lines[k][0][ci], 'parts':[entry[3]]}
                
                break
        if cont:
            break

print('')
print('part 1:', s)

####

gearprodsum = 0
for k,v in store.items():
    if v['symbol'] == '*' and len(v['parts'])==2:
        gearprodsum += v['parts'][0]*v['parts'][1]

print('part 2:', gearprodsum)




