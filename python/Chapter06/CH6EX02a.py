def what_is_this(*args):
    typeList=[]
    for x in args:
        for y in x:
            typeList.append(id(y))
    return(typeList)
