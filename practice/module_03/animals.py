
class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"

    def speak(self):
        return "..."
    def describe(self):
        return f"{self.name} says {self.speak()})"




class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"


class Dog(Animal):
    def __init__(self, name,tricks):
        super().__init__(name)
        self.tricks = tricks
    def speak(self):
        return "woof"
class Horse(Animal):
    def __init__(self,name,height,):

        super().__init__(name)
        self.height = height
    def speak(self):
        return "Neigh"


    def describe(self):
        return f"{super().describe()} and is {self.height} cm tall"


luna=Cat("Luna")
rex= Dog("Rex",["Sit","Shake"])

for animal in [luna,rex]:
    print(f"{animal.name}, says: {animal.speak()}")
print("\nRex´s tricks: ", rex.tricks)
print("Rex is an animal: ", isinstance(rex, Animal))
