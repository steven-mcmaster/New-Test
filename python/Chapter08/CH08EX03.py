numsum=0
while True:
    try:
        numsum+=int(input('gimme a number: '))
    except ValueError:
        pass    
    except KeyboardInterrupt:
        print("\nI'm sorry Dave, I can't let you do that")
    except EOFError:
        print("FINE!\nyour total is:  " , numsum)
       
        break

        
