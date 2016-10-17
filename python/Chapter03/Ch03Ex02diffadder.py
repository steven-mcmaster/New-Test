#! usr/bin/env python3
num1 = float(input("Please enter a number"))
num2 = float(input("Please enter another number"))
total=0
if num2 > num1:
    num1, num2 = num2,num1
while num1 >= num2:
    total = total + num2
    num2 +=1 
print (total)
