uniwords=set()
while True:
    data = input("enter stuff:  q to quit")
    if data == 'q':
        break
    uniwords.update(data.split(" "))
print(sorted(uniwords))
print(str(len(uniwords))+"   unique words")
