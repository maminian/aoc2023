import csv

with open('input', 'r') as f:
    csvr = csv.reader(f)
    lines = list(csvr)

# part 1
cals = []
for line in lines:
    f,l = '', ''
    for char in line[0]:
        if char in '1234567890':
            if len(f)==0:
                f=char
            l = char
    cals.append( int(f+l) )

print(sum(cals))

# part two...
words = ['zero', 'one', 'two', 'three', 'four', 
            'five', 'six', 'seven', 'eight', 'nine']

cals2 = []
for line in lines:
    f,l = '', ''
    for i,char in enumerate(line[0]):
        if char in '1234567890':
            if len(f)==0:
                f=char
            l = char
        else:
            for j,w in enumerate(words):
                # try to match following text with words zero through nine.
                if line[0][i:i+len(w)] == w:
                    # winner winner
                    if len(f)==0:
                        f=str(j)
                    l = str(j)
    cals2.append( int(f+l) )

print(sum(cals2))

