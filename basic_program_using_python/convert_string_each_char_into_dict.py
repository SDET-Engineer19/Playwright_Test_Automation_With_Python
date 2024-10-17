word = "Programming"
word = word.lower()
word_dict = {}
word_dict = dict.fromkeys(word, 0)
for val in word:
    word_dict[val] += 1


print(word_dict)
print(type(word_dict))
