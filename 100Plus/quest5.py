#---------------------------------------------------------------------------------# 
## Define a class which has at least two methods: ##
## getString: to get a string from console input ##
## printString: to print the string in upper case. ##
#---------------------------------------------------------------------------------# 

class InputOutString(object):
    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s())

strObj = InputOutString()
strObj.getString()
strObj.printString()
