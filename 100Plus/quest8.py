
words = [str(x) for x in input('Enter list of words separated by commas: ').split(',')]

words.sort()
print(','.join(words))
