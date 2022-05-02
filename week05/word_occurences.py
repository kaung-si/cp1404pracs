word_to_count = {}
text = input("Enter a string: ")
texts = text.split()
max_length = 0
for x in texts:
    if len(x) > max_length:
        max_length = len(x)
texts.sort()
for word in texts:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
for word in word_to_count:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
