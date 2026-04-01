from animal import Animal

# these class attributes are an example of inheritance

class Cat(Animal):
    
    #super. says to pull from one class above and come back.

    def __init__(self, name, species, color):
        super().__init__(name, species) 
        self.color = color 

    def __str__(self):
        return super().__str__() + f"Color: {self.color}\n"
    
    def speak(self):
        print(f"{self.name} meows!\n")