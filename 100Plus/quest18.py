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
w = re.findall(r'[$#@]', passwd)
x = re.findall(r'[a-z]', passwd) 
y = re.findall(r'[A-Z]', passwd)
z = re.findall(r'[0-9]', passwd)

if 6 < len(passwd) < 12 and w and x and y and z:
    print('Your password is accepted')
else:
    print('Password rejected')