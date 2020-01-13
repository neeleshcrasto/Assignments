#-------------------------------------------------------------------------------------#
## This accepts a comma separated sequence of words as input ##
## Then prints the words in a comma-separated sequence after sorting them alphabetically ##
#-------------------------------------------------------------------------------------#

words = [str(x) for x in input('Enter list of words separated by commas: ').split(',')]

words.sort()
print(','.join(words))
