
if __name__ == '__main__':
    n = int(input())
    lists = []
    for i in range(n):
        mip = [(x) for x in input().split(' ')]
        if mip[0] == "insert":
            lists.insert(int(mip[1]), int(mip[2]))
        if mip[0] == "remove":
            lists.remove(int(mip[1]))
        if mip[0] == "append":
            lists.append(int(mip[1]))
        if mip[0] == "sort":
            lists.sort()
        if mip[0] == "pop":
            lists.pop()
        if mip[0] == "reverse":
            lists.reverse()
        if mip[0] == "print":
            print(lists)


