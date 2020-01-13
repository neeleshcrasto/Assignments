#-------------------------------------------------------------------------------------#
## This accepts sequence of lines as input  ##
## Then prints the lines after making all characters in the sentence capitalized ##
#-------------------------------------------------------------------------------------#

lines = [str(x) for x in input('Enter list of lines separated by commas:\n ').split(',')]
print(lines)

for line in lines:
    print(line.upper())
