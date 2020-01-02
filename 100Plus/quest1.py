#------------------------------------------------------------------------------------# 
## Program to find all numbers which are divisible by 7 but are not a multiple of 5 ##
## within a given range ##
#------------------------------------------------------------------------------------# 

a = int(input('Enter the first range of number:'))
b = int(input('Enter the second range of number:'))
lst = []
for i in range(a, b):
    if i%7 == 0 and i%5 != 0:
        lst.append(i)

print(lst)
