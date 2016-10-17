def sort(olist):
    return sorted(olist)


def reverse(olist):
 #   nlist = sorted(olist)
    nlist=[]
    for x in olist:
        nlist.insert(0,x)
    return nlist
values = [10,40,30,20,5]


print (sort(values))
print (reverse(values))
print (reverse(sort(values)))
print (values)
