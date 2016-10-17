def big_list_maker(*args):
    oneList = []
#    print(type(args))
    for x in args:
        oneList.append(x)
    return(oneList)
#    for x in oneList:
#        print(x)
#newList = big_list_maker([1,2,3],[1,2,5],66,"g")
def what_is_this(*args):

    typeList=[]
    for x in args:
        for y in x:
            typeList.append(type(y))
    return(typeList)


#print(get_types(newList))
