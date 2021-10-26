import  collections

no_of_words = int(input())

w_dict = collections.OrderedDict()

for i in range(no_of_words):
    word = input()
    if word in w_dict:
        w_dict[word] +=1
    else:
        w_dict[word] = 1

print(len(w_dict))

for key, value in w_dict.items():
    print(value, end=' ')