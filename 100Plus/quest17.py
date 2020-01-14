
#-------------------------------------------------------------------------------------------------# 
## This program computes the net amount of a bank account based a transaction log from input ##
## The transaction log format is shown as following - D is deposit / W is withdrawal ##
#-------------------------------------------------------------------------------------------------#
import re

balance = 0
transaction = 0
while transaction != 'q':
    transaction = input('Enter the transaction(q to quit):')

    amount = re.findall(r'\d+', transaction)
    print(amount)
    if transaction[0] == 'D':
        balance = balance + int(amount[0])
    elif transaction[0] == 'W':
        balance = balance - int(amount[0])
print('Final balance:',balance)
