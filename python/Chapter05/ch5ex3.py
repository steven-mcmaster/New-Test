def bigfun(num1,num2):
    def smallfun():
        nonlocal num1, num2
        return (num1+num2)
    return smallfun()
    
print(bigfun(2,3))
