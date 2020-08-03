from collections import Counter

"""
input: 
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
"""
if __name__ == "__main__":
    _ = input()
    count = Counter(list(map(int, input().split())))
    no_of_customers = int(input())
    res = 0
    for _ in range(no_of_customers):
        line = list(map(int, input().split()))
        if count[line[0]] != 0:
            res += line[1]
            count[line[0]] -= 1
    print(res)
