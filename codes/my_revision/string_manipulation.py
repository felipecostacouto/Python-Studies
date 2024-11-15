
# strip remove whitespaces
# join reunites a string
# split - divide a string [list]
word = 'Look , this is interesting   '
word_split = word.split()

for i, word in enumerate(word_split):
   word_split[i] = word_split[i].strip()

print(word_split)

words_united = ''.join(word_split)
print(words_united)

