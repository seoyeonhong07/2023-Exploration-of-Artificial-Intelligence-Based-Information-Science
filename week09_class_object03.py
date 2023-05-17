class Pokemon:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp


    def say(self):
        print(f"I'm a pokemon. My name is {self.name}")


class Pikachu(Pokemon):   # is-a relationship
    pass


class Squirtle(Pokemon):
    pass


class Digimon:
    pass

if __name__ == "__main__":
    #pikachu.say()

    pikachu = Pikachu("pikachu", 1, 35)

    pikachu.say()

    squirtle = Squirtle("squirtle", 1, 44)
    charizard = Pokemon("charizard", 36, 78)
    charizard.say()

    print(squirtle.name)
    print(pikachu.name)
    print(issubclass(Squirtle, Pokemon))
    print(issubclass(charizard, Pokemon))
