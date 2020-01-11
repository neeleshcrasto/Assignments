#------------------------------------------------------------------------------------------------------------------# 
## Take a sentence as input and prints the words after removing duplicate words and sorting alphanumerically. ##
#------------------------------------------------------------------------------------------------------------------# 

lines = [str(x) for x in input('Enter your sentence: ').split(' ')]
print(lines)

lines = list(dict.fromkeys(lines))

lines.sort()
print(' '.join(lines))