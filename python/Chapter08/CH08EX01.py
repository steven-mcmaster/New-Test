listnums=[1,2,3,4,5,6,7,8,9,10]
while True:
    usrnum=(input("gimme a number fool:  "))
    try:
        if int(usrnum) < 0:
            raise IndexError
        print(listnums[int(usrnum)])
    except IndexError:
        print("You suck gimme a diff num")
    except ValueError:
        if usrnum == "end":
            break
        print('dis a ValueError (try a number fool)')
