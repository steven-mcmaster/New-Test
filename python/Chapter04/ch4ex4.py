uniwords=set()
worddict={}
while True:
    data = input("enter stuff:  q to quit")
    if data == 'q':
        break
    data=data.split(" ")
    for x in data:
        if x in worddict.keys():
            worddict[x]+=1
        else:
            worddict[x]=1
        uniwords.update(data)
for x in sorted(worddict.keys()):
	print(x,worddict[x])
dictlist= list(worddict.keys())
dictlist.sort(key=worddict.get)
for x in dictlist:
	print(x,worddict[x])
	


