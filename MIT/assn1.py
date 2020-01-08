
from math import *

# ----------------------------#
## COMPUTING PRIMES NUMBERS ##
# ----------------------------#

# function to compute product of primes
product = log(2)
def prdtprime (prdt):
    global product
    product = product + log(prdt)
    return product


# function to check whether a number is prime
def pcheck(prim):
    i = 2
    global x
    x = 0
    while i < (prim/2):
        check = prim%i
        if check == 0:
            x = 2
            return None
        elif check != 0:
            i = i + 1
    # print(prim,'is a prime number')

n = int(input('Enter which n(th) Prime number you want: '))

# for first prime number
if n == 1:
    prime = 2
    print ('The no.',n,'prime number is', prime)

# Generate number
if n > 1:
    nos = 1
    i = 2
    iter = 1
    while iter != n:
        nos = nos + 2
        pcheck(nos)
        if x == 2:
            pass
        else:
            iter = iter + 1
            prdtprime(nos)
            # print(nos,'is a prime number')
            
    print('The number',n,'prime number is ',nos)
        
# ----------------------------#
## PRODUCT OF THE PRIMES ##
# ----------------------------#


print('The product is ', product)


# check if number is prime & print it out