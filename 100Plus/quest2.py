#------------------------# 
## Factorial program ##
#------------------------# 

number = int(input('Enter the number for which factorial is required:'))
factorial = 1
for number in range(1, number):
    number = number + 1
    factorial = factorial*number

print('Factorial of',number,'is',factorial)
