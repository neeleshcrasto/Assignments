from math import sqrt

c = 50; h = 30
d = []; q = []

for i in range(0,3):
    i = int(input('Enter value of D (Press q to quit):'))
    d.append(i)

# print(d)

for i in range(0,3):
    i = round(sqrt((2*c*d[i])//h))
    q.append(i)

print('The result:',q)


