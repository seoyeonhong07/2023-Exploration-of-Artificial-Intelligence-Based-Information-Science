class Animal:
    def says(self):
        return 'CRY!'

class Horse(Animal):
    def says(self):
        return '이히힝!'

class Donkey(Animal):
    def says(self):
        return '나귀 나귀~'

class Mule(Donkey, Horse):
    pass
#    def says(self):
#        return '노새 노새 젊어서 노새~'

class Hinny(Horse, Donkey):
    pass

if __name__ == "__main__":
    m1 = Mule()
    h1 = Hinny()
    print(m1.says())
    print(Mule.mro())
    print(h1.says())