import sys
print(len(sys.argv))
sys.argv.pop(0)
listthing=[]
for x in sys.argv:
    listthing.append(int(x))
print(sorted(listthing))

