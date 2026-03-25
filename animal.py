class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects

    # TODO create the initializer for Animal with name and species as attributs

    #object specfic attributes constructor/ initializer 
    def __init__(self, name, species):
        self.name= name
        self.species= species

    # class method
    def speak(self):
        print(f"{self.name} makes a noise\n")

    # magic method changes how print object behaves orverrides the print method
    def __str__(self):
        return f"Kingdom: {self.kingdom}\nName: {self.name}\nSpecies: {self.species}\n"


