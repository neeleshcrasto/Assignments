
#-----------------------------------------------------------------------------------------------------------# 
## All numbers between a given range (both included) such that each digit of the number is an even number ##
#-----------------------------------------------------------------------------------------------------------# 

x, y = map(int, input('Enter the range between which you want to find the numbers:').split(','))
# print('Range is',x,'to',y)
newlist = []
for i in range(x,y):
    numberlist = [int(j) for j in str(i)]
    for number in numberlist:
        # print(number)
        if number == 0 or number%2 == 0:
            continue
        elif number%2 != 0:
            break
        newlist.append(i)

print(newlist)

