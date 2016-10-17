import sys
sys.argv.pop(0)
linecounter = 0
wordcounter = 0
charcounter = 0
if sys.argv[0] == '-t':
    #print("asdfadsdadasdad")
    sys.argv.pop(0)
    for filename in sys.argv:
        with open(filename,'r') as realfile:
            filetext = realfile.readlines()
            #linecounter = 0
            #wordcounter = 0
            #charcounter = 0
            for line in filetext:
                linecounter += 1
                for char in line:
                    charcounter += 1
                line = line.split()
                for word in line:
                    wordcounter +=1

            #print(charcounter, wordcounter, linecounter)
    print(charcounter, wordcounter, linecounter)
else:
    for filename in sys.argv:
        with open(filename,'r') as realfile:
            filetext = realfile.readlines()
            linecounter = 0
            wordcounter = 0
            charcounter = 0
            for line in filetext:
                linecounter += 1
                for char in line:
                    charcounter += 1
                line = line.split()
                for word in line:
                    wordcounter +=1

            print(charcounter, wordcounter, linecounter)
