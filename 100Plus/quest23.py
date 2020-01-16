#------------------------------------------------------------------------------------# 
## Write a method which can calculate square value of number ##
#------------------------------------------------------------------------------------# 

nummer = int(input('Enter the number:'))

def makesquare(n):
    n = n**2
    return n

sqno = makesquare(nummer)
print('Square of',nummer,'is',sqno)
