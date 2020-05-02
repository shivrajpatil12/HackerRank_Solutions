from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    d = OrderedDict()
    for i in range(n):
        item = input().split()
        item_price = int(item[-1])
        item_name = " ".join(item[:-1])
        if d.get(item_name):
            d[item_name] += item_price
        else:
            d[item_name] = item_price
    for item_name, item_price in d.items():
        print(item_name , item_price)


""" 2nd method """
# from collections import OrderedDict
# my_order = OrderedDict()
# for i in range(int(input())):
#     name,space,price = input().rpartition(' ')
#     if name not in my_order:
#         my_order[name] = int(price)
#     else:
#         my_order[name] += int(price)
# for item_name, net_price in my_order.items():
#     print(item_name,net_price)
