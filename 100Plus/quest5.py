#---------------------------------------------------------------------------------# 
## Define a class which has at least two methods: ##
## getString: to get a string from console input ##
## printString: to print the string in upper case. ##
#---------------------------------------------------------------------------------# 

class InputOutString():
    def getString(self):
        s = input('Enter input here: ')
        return s

    def printString(self):
        print('We got this string:',x)

strObj = InputOutString()
x = strObj.getString()
strObj.printString()


# class A(object):
#     def __init__(self):
#         self.x = 'Hello'

#     def method_a(self, foo):
#         print (self.x + ' ' + foo)

# a = A()               # We do not pass any argument to the __init__ method
# a.method_a('Sailor!') # We only pass a single argument
