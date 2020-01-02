#---------------------------------------------------------------------------------# 
## Accept a string of comma separated values and print out as list & tuple ##
#---------------------------------------------------------------------------------# 

values = input('Enter values separated by comma\n')
liszt = values.split(",")
toppel = tuple(liszt)

print(liszt)
print(toppel)

