from collections import deque
d = deque()
for _ in range(int(input())):
    
    operation= input().split()
    if operation[0] == "append":
        d.append(operation[1])
    if operation[0] == "appendleft":
        d.appendleft(operation[1])
    if operation[0] == "popleft":
        d.popleft()
    if operation[0] == "pop":
        d.pop()

for i in range(len(d)):
    print(d[i], end=" ")
