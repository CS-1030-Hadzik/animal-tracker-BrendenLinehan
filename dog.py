from animal import Animal

#child class of animal
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    def __init__(self, name, species, size):
        super().__init__(name, species) 
        self.size = size 

    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n"
    

    def speak(self):
        print(f"{self.name} woofs!\n")