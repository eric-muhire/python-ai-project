
class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def speak(self):
        return "Meow"

        return

class Dog(Animal):
    def __init__(self, name,tricks):
        super().__init__(name)
        self.tricks = tricks
    def speak(self):
        return "woof"

luna=Cat("Luna")
rex= Dog("Rex",["Sit","Shake"])

for animal in [luna,rex]:
    print(f"{animal.name}, says: {animal.speak()}")
print("\nRex´s tricks: ", rex.tricks)
print("Rex is an animal: ", isinstance(rex, Animal))
