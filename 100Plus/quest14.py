#--------------------------------------------------------------------------------------------------# 
## This program accepts a sentence and calculates the number of upper case and lower case letters ##
#--------------------------------------------------------------------------------------------------#
 
sentence = str(input('Enter your sentence: '))
upcase = 0
locase = 0

for alphabet in sentence:
    asciival = ord(alphabet)
    if 64 < asciival < 91:
        upcase = upcase + 1
    elif 96 < asciival < 123:
        locase = locase + 1

print('No. of upper case letters:',upcase)
print('No. of lower case letters:',locase)
