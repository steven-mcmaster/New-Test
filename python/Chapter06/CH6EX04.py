import sys
print(len(sys.argv))
sys.argv.pop(0)
total=0
for x in sys.argv:
    total+=int(x)
print (total)
print (total/len(sys.argv))

