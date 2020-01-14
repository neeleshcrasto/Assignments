#-------------------------------------------------------------------------------------------------# 
## Square each odd number in a list. The list is input by a sequence of comma-separated numbers. ##
#-------------------------------------------------------------------------------------------------#

nos = [int(x) for x in input('Enter list of numbers separated by commas: ').split(',')]
noi = []
for no in nos:
    if no%2 != 0:
        nodd = no**2
        noi.append(nodd)

print(noi)

