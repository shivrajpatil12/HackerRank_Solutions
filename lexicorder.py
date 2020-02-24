import itertools

x = 1
y = 1
z = 1
n = 2

print([list(coords)
       for coords in itertools.product(range(x+1), range(y+1), range(z+1))
       if sum(coords) != n])
