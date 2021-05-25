len_array, len_sets = (int(i) for i in input().split())
arr = map(int, input().strip().split(' '))
set_A = set(map(int, input().strip().split(' ')))
set_B = set(map(int, input().strip().split(' ')))
happiness = 0
for i in arr:
    if i in set_A:
        happiness += 1
    if i in set_B:
        happiness += -1
print(happiness)

