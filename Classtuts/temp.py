
class Temperature():
    def __init__(self, num):
        self.num = num

    def Cel2Fahr(self):
        Fahr = ((self.num*9)/5)+32
        return Fahr

    def Fahr2Cel(self):
        Cel = (self.num - 32)*(5/9)
        return Cel

print('This takes temperature and converts it into Celsius or Fahrenheit. Temperature to be followed by C or F')

raw_input = input('Enter temperature (in C or F)')
CorF = raw_input[-1]
number = int(raw_input[:-1])

if CorF == 'C':
    convert = Temperature(number).Cel2Fahr()
    print(number,'Celsius is equal to','{0:.2f}'.format(convert),'Fahrenheit')
elif CorF == 'F':
    convert = Temperature(number).Fahr2Cel()
    print(number,'Fahrenheit is equal to','{0:.2f}'.format(convert),'Celsius')
