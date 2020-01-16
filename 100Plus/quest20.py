
#------------------------------------------------------------------------------------# 
## Define a class with a generator which can give numbers, which are divisible by 7 ##
## Between a given range 0 and n. ##
#------------------------------------------------------------------------------------# 

nummer = int(input('Range upto which number is desired:'))

def rangedivider(n):
    numlist = []
    for i in range(0,n):
        if i%7 == 0:
            numlist.append(i)
    return numlist

print(rangedivider(nummer))

