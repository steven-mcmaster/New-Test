def bigfun():
    def smallfun(num1,num2):
        return (num1+num2)
    return smallfun(number1,number2)
number1 = 3
number2 = 5
print(bigfun())
