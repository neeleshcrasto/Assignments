
#-------------------------------------------------------------------------------------------# 
## This program computes the value of a+aa+aaa+aaaa with a given digit as the value of a. ##
#-------------------------------------------------------------------------------------------#
 
nummer = int(input('Enter the number: '))
nummer = str(nummer)
nummer2 = str(nummer+nummer)
nummer3 = str(nummer+nummer+nummer)
nummer4 = str(nummer+nummer+nummer+nummer)

finalnummer = int(nummer) + int(nummer2) + int(nummer3) + int(nummer4)

print('The result is',finalnummer)
