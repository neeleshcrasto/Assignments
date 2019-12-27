#---------------------------------#
## 6a + 9b + 20c = n ##
#---------------------------------#

import numpy

#---------------------------------#
## Solution to Problem 1 ##
#---------------------------------#

n = int(input('Enter number of McNuggets you want:'))

lists = [6, 9, 15, 20, 26, 29, 35]

def secondlvl(rem):
    rem2 = rem%list
    if rem2 in lists or rem2 == 0:
        print(n//list,'buxes of',list,'McNuggets')
        print('1 bux of',rem2,'McNuggets')
        quit()



for list in lists:
    rem = n%list
    if rem in lists or rem == 0:
        print(n//list,'boxes of',list,'McNuggets')
        print('1 box of',rem,'McNuggets')
        quit()
            
secondlvl(rem)


print(n,'McNuggets cannot be purchased')

# intc = n // 20
# intb = n // 9
# inta = n // 6

# intab = n // 15
# intac = n // 26
# intbc = n // 29

# intabc = n // 35

# rema = n%6
# remb = n%9
# remc = n%20

# remab = n%15
# remac = n%26
# rembc = n%29

# remabc = n%35

# print('a=',inta,',b=',intb,',c=',intc,',ab=',intab,',ac=',intac,',bc=',intbc,',abc=',intabc)
# print('rem a=',rema,',rem b=',remb,', rem c=',remc,', rem ab=',remab,', rem ac=',remac,', rem bc=',rembc,', rem abc=',remabc)