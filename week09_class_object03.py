class Pokemon:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp


    def say(self):
        print(f"I'm a pokemon. My name is {self.name}")

    def attack(self):
        print(f"{self.name} launches an area attack.")


    def attack_target(self, target):
        print(f"{self.name} attacks {target}!")



class Pikachu(Pokemon):   # is-a relationship
    def attack(self):
        print(f"{self.name} launches an area-of-effect electric attack.")


    def attack_target(self, target):
        print(f"{self.name} launches an electric attack on {target}!")


class Squirtle(Pokemon):
    def attack(self):
        print(f"{self.name} casts a wide-area water cannon attack.")

    def attack_target(self, target):
        print(f"{self.name} casts a water cannon attack on {target}!")


class Charizard(Pokemon):
    def attack(self):   # derived class method, override
        super().attack()   # base class method
        print(f"{self.name} casts a wide-area fire attack.")

    def attack_target(self, target):
        print(f"{self.name} casts a fire attack on {target}!")


class Digimon:
    pass


if __name__ == "__main__":
    #pikachu.say()
    pikachu = Pikachu("pikachu", 1, 35)
    pikachu.say()
    squirtle = Squirtle("squirtle", 1, 44)
    charizard = Charizard("charizard", 36, 78)
    charizard.say()


    pikachu.attack_target(squirtle.name)
    charizard.attack()
    pikachu.attack()
    squirtle.attack()

    print(squirtle.name)
    print(pikachu.name)
    print(issubclass(Squirtle, Pokemon))
    print(issubclass(Charizard, Pokemon))
