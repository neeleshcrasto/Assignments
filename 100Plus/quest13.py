#-------------------------------------------------------------------------------------------# 
## This program accepts a sentence and calculates the number of letters and digits. ##
#-------------------------------------------------------------------------------------------#
 
sentence = str(input('Enter your sentence: '))
numberr = 0
letter = 0

for alphabet in sentence:
    asciival = ord(alphabet)
    if 64 < asciival < 91 or 96 < asciival < 123:
        letter = letter + 1
    elif 47 < asciival < 58:
        numberr = numberr + 1

print('The number of letter is',letter,', number of digits is',numberr)
