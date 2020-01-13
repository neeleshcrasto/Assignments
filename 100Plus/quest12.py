
#-----------------------------------------------------------------------------------------------------------# 
## All numbers between a given range (both included) such that each digit of the number is an even number ##
#-----------------------------------------------------------------------------------------------------------# 

x, y = map(int, input('Enter the range between which you want to find the numbers:').split(','))
# print('Range is',x,'to',y)
newlist = []
for i in range(x,y):
    numberlist = [int(j) for j in str(i)]
    newnumlist = []
    for number in numberlist:
        if number == 0 or number%2 == 0:
            number = 0
        elif number%2 != 0:
            number = 1
        newnumlist.append(number)
    # print(newnumlist)
    if sum(newnumlist) == 0:
        newlist.append(i)
    # print(i)

print(newlist)

