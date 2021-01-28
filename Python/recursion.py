from __future__ import print_function, division
import math

# Generate a numerical value of pi using Ramanujan's approximation
# https://greenteapress.com/thinkpython2/html/thinkpython2008.html

def estimate_pi():
    k = 0; total = 0
    while True:
        print(k)
        first_var = (2*math.sqrt(2)) / 9801
        secnd_var = (math.factorial(4*k)*(1103+26390*k)) / ((math.factorial(k)**4) * (396**(4*k)))
        term = (first_var * secnd_var)
        total += term
        if abs(term) < 1e-15:
            break
        k += 1
    return 1 / total

print(estimate_pi())



# Get the GCD of two given numbers

a = int(input('What is the first number?'))
b = int(input('and second number?'))


def getgcd(a, b):
    if a % b != 0:
        r = a % b
        getgcd(b, r)
    else:
        return print('The GCD is', b)

if a > b:
    getgcd(a, b)
else:
    getgcd(b, a)

