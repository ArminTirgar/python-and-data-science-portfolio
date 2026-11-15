
class Animal:

    zoo_name = "Kerman Zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def __str__(self):
        return f'{self.name}-{self.species}-{self.age}'

    def make_sound(self):
        return self.sound

    def info(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")
        print(f"Age : {self.age}")
        print(f"Sound : {self.sound}")
        print(f"Zoo name : {self.zoo_name}")


class Bird(Animal):

    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} says : {self.sound}"


lion = Animal("Simba", "Mammal", 12, "Roar!")
parrot = Bird("Rio", "Bird", 3, "Hello!", 25)


print("===== Animal Class =====")

print(lion)
print(lion.make_sound())
lion.info()



print("\n===== Bird Class =====")

print(parrot)
print(parrot.make_sound())
parrot.info()
