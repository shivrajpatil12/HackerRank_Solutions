# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

n1 = int(input())
set_1 = set(map(int, input().split()))
n2 = int(input())
set_2 = set(map(int, input().split()))
print(len(set_1-set_2))