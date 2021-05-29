"""
method used:
The eval() method parses the expression passed to this method and runs python expression (code) within the program.
"""
# Input
# 1 4
# x**3 + x**2 + x + 1


x, k = map(int, input().strip().split())
exp = input()

if eval(exp) == k:
    print(True)
else:
    print(False)