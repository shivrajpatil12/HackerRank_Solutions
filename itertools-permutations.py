# input:- demo 2

from itertools import permutations

st, ln = input().split()
for i in permutations(sorted(st), int(ln)):
    print(''.join(i))

