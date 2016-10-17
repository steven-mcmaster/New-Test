def thing(*args,num):
    count = 0
    for x in args:
        if int(x) > num:
            count += 1
    return count      
#print(positive([5, -10, 10, -20, 30]))
