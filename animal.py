class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects

    # TODO create the initializer for Animal with name and species as attributs

    #object specfic attributes
    def __init__(self, name, species):
        self.name= name
        self.species= species

    def speak(self):
        print(f"{self.name} makes a noise")

    def __str__(self):
        return f"Kingdom: {self.kingdom}\nName: {self.name}\nSpecies: {self.species}"


