import operator

word = input()
word_list = list(word)

word_dict = dict()

for i in word_list:
    word_dict[i] = word_dict.get(i, 0)+1

sort_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))

count = 0
for key, val in sort_dict.items():
    if count < 3:
        print(key, val)
        count += 1


