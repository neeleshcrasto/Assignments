#---------------------------------#
## 6a + 9b + 20c = n ##
#---------------------------------#

#---------------------------------#
## Solution to Problem 1 ##
#---------------------------------#

n = int(input('Enter number of McNuggets you want:'))

intc = n // 20
intb = n // 9
inta = n // 6

intab = n // 15
intac = n // 26
intbc = n // 29

intabc = n // 35

rema = n%6
remb = n%9
remc = n%20

remab = n%15
remac = n%26
rembc = n%29

remabc = n%35

print('a=',inta,',b=',intb,',c=',intc,',ab=',intab,',ac=',intac,',bc=',intbc,',abc=',intabc)
print('rem a=',rema,',rem b=',remb,', rem c=',remc,', rem ab=',remab,', rem ac=',remac,', rem bc=',rembc,', rem abc=',remabc)