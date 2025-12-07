from itertools import accumulate as acc

a, b = [50], [50]

for line in open('input.txt'):
    dir = {'L': -1, 'R': +1}[line[0]]
    dist = int(line[1:])
    a += [dir * dist]
    b += [dir] * dist

for x in a, b:
    print(sum(x%100==0 for x in acc(x)))