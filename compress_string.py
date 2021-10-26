from itertools import *

input_str = input()

for i, v in groupby(map(int, list(input_str))):
    print(tuple([len(list(v)), i]), end=" ")




