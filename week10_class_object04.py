# week10_class_object04

class PrettyMixin:
    def dump(self):
        print(f'{self.name} pokemon')
        import pprint
        pprint.pprint(vars(self))


class Pokemon(PrettyMixin):
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


if __name__ == "__main__":
    p1 = Pokemon("pikachu", 35, 1)
    p2 = Pokemon("squirtle", 40, 1)
    p1.dump()
    p2.dump()

