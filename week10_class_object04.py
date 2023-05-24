# week10_class_object04

class PrettyMixin:
    def dump(self):
        print(f'{self.name} pokemon')
        import pprint
        pprint.pprint(vars(self))


class Pokemon(PrettyMixin):
    def __init__(self, input_name, hp, level):
        self.hidden_name = input_name
        self.hp = hp
        self.level = level


    def get_name(self):
        print("getter executed!")
        return self.hidden_name


    def set_name(self, input_name):
        print("setter executed!")
        self.hidden_name = input_name


    def info(self):
        print("=================")
        print(f'Name : {self.hidden_name}')
        print(f'Hp : {self.hp}')
        print(f'Level : {self.level}')
        print("=================")

    name = property(get_name, set_name)


if __name__ == "__main__":
    p1 = Pokemon("pikachu", 35, 1)
    p2 = Pokemon("squirtle", 40, 1)
    p2.info()   # Pokemon.info(p2)
    p1.dump()
    p2.dump()
    p2.level = 2   # direct access
    p2.info()
    p2.name = "watortle"
    print(p2.name)

