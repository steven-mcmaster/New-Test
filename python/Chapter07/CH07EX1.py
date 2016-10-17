

'''
problem with kids/adding

'''


class Person:
    def __init__(self,name,age,dontgenderme):
        self.name = name
        self.age = age
        self.dontgenderme = dontgenderme
        
    def __str__(self):
        return self.name + str(self.age) + self.dontgenderme
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self, age):
        self._age = age
        
    @property
    def dontgenderme(self):
        return self._dontgenderme
        
    @dontgenderme.setter
    def dontgenderme(self, dontgenderme):
        self._dontgenderme = dontgenderme

class Family:
    def __init__(self, mommy, othermommy, *kids):
        self.mommy = mommy
        self.othermommy = othermommy
        self.kids = kids

    def __str__(self):
        return str(self.mommy) + '  ' + str(self.othermommy) + '  ' + \
        str(self.kids)#' AND '.join(self.kids)
    
    def add(self, newkid):
        print(self.kids[0], self.kids[1], '*********')# self.kids [2] )
        self.kids.append(newkid)
        
    def __lt__(self, naaaybor):
        if len(self.kids) < len(naaaybor.kids):
            return True
        else:
            return False
      
    def __gt__(self, naaaybor):
        if len(self.kids) > len(naaaybor.kids):
            return True
        else:
            return False
    
    def __eq__(self, naaaybor):
        if len(self.kids) == len(naaaybor.kids): 
            return True
        else:
            return False       

class Worker:
    pass

def main():
    p1=Person('tom', 32, 'never')
    p2=Person('toasdm', 3232, 'neverdf')
    print(p1)
    print(p2)
    f1 = Family(p1, p2,'qwde1','12da','321dfs')

    print(f1)
    p3=Person('richyrich', 11, 'nopes')
    #f2.add(p3)
    f2 = Family(p1, p2, p3, 'asd')
    print(f2)
    print(f1 == f2)

if __name__ == "__main__":main()
