l = ['hello world', 'hello python', 'python is great']
word = {}

# add word to dict
for idx, sentence in enumerate(l):
    words = sentence.split(' ')
    for c in words:
        if c not in word:
            word[c] = []
        word[c].append(idx)


print(word)