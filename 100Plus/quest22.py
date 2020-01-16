#------------------------------------------------------------------------------------# 
## Write a program to compute the frequency of the words from the input ##
## The output should output after sorting the key alphanumerically ##
#------------------------------------------------------------------------------------# 
from collections import Counter

sentence = str(input('Enter your sentence: '))

words = sentence.split(' ')
sortedlist = words.sort()
sortsentence = ' '.join(words)
print('Sorted list:', sortsentence)

words_count = Counter(words)
uniq_words = list(set(words))

for words in uniq_words:
    print(words, words_count[words])