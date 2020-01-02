#------------------------------------------------------# 
## List of numbers with squares in dictionary format ##
#------------------------------------------------------# 

number = int(input('Enter number up to which squares are required:')) 
sqlstdict = {}
for square in range(1, (number+1)):
    sqlstdict[square] = square**2

print('Final',sqlstdict)
