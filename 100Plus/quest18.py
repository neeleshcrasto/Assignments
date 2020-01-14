#---------------------------------------------------------------# 
## This program checks the validity of password input by users.
## Following are the criteria for checking the password: ##
## 1. At least 1 letter between [a-z] ##
## 2. At least 1 number between [0-9] ##
## 1. At least 1 letter between [A-Z] ##
## 3. At least 1 character from [$#@] ##
## 4. Minimum length of transaction password: 6 ##
## 5. Maximum length of transaction password: 12 ##
#---------------------------------------------------------------#
import re

passwd = str(input('Enter your password: '))
x = re.search("@", passwd)
print(x)

if 6 < len(passwd) < 12 and passwd.isalpha() and passwd.isdigit() and True:
    print('Your password is accepted')
else:
    print('Password rejected')