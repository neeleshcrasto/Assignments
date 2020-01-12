#---------------------------------------------------------------------------------------------------------# 
## Takes 4 digit numbers as input. Only numbers divisible by 5 are printed in a comma separated sequence ##
#---------------------------------------------------------------------------------------------------------# 

lines = [int(x) for x in input('Enter the list of numbers: ').split(',')]

for line in lines:
    if line%5 == 0:
        print(line,end=',')
print('\n')


