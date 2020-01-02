a = int(input('Enter the first range of number:'))
b = int(input('Enter the second range of number:'))
lst = []
for i in range(a, b):
    if i%7 == 0 and i%5 != 0:
        lst.append(i)

print(lst)
