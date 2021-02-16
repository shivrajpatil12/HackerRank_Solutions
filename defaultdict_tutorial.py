

from collections import  defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(0, n):
    d[input()].append(i+1)

for i in range(0, m):
    print(*d[input()] or [-1])



