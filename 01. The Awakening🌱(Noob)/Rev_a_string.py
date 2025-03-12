word = input("Enter a word: ")

rev_word = ''
for i in range(len(word)-1, -1, -1):
    rev_word = rev_word +  word[i]

print(rev_word)