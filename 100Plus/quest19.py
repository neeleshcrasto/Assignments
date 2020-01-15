#----------------------------------------------------------------------# 
## This program sorts by (name, age, height) tuples in ascending order ##
## Name is string, age and height are numbers. ##
## The tuples are input by console. The sort criteria is: ##
## 1: Sort based on name; ##
## 2: Then sort based on age; ##
## 3: Then sort by score. ##
## The priority is that name > age > score. ##
#----------------------------------------------------------------------#
from operator import itemgetter

fulist = []
while True:
    entry = input('Enter data:')
    if not entry:
        break
    fulist.append(tuple(entry.split(',')))

print('Original list:',fulist)

print('Sorted list:',sorted(fulist, key=itemgetter(0,1,2)))



