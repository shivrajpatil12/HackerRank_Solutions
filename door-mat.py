rows, col = map(int, input().split())
width = col
for i in range(0, int(rows/2)):
    s = ".|."*((2*i)+1)
    print(s.center(width, '-'))
print("WELCOME".center(width, '-'))

i = int(rows/2)
while i > 0:
    s = ".|." * ((2 * i) - 1)
    print(s.center(width, '-'))
    i = i-1

# alternative
# N,M=map(int,input().split())
# a=[('.|.'*i).center(M,'-') for i in range(1,N,2)]
# for e in a+['WELCOME'.center(M,'-')]+list(reversed(a)):print(e)