#! usr/bin/env python3
usrString = input("Please enter some text")
print("This ends in a '.' : " , usrString.endswith("."))
print("This has only letters : " , usrString.isalpha())
print("This has an 'x' in it : " , 'x' in usrString) # or bool((usrString.find("x")+1)))
print("I changed your 'e\'s' to 'E\'s' : " , usrString.replace('e','E'))
