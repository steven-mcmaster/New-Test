#! usr/bin/env python3
numbers=(input("Enter some numbers (use a space to seperate)")).split(" ")
#print(type(numbers))
#print(len(numbers))
for num in numbers:
    if float(num)>0:
        print(num)

