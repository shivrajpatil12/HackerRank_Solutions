from itertools import product

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
print(*product(x, y))
