from animal import Animal

#child class of animal
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    def __init__(self, name, species, size):
        super().__init__(name, species) 
        self.size = size 
        self.__age = 0 #encapsulation __ makes it a private data member in python

    #public method that allows users to get age of the dog
    # getter
    def get_age(self):
        return self.__age


    #setter for encapsulation
    def set_age(self, new_age):
        if new_age < 0:
            return print("The age needs to be positive")
        self.__age = new_age
        self.print_dog_age()

    def print_dog_age(self):
        print( f"{self.name}'s age is now {self.__age}")

    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n"
    

    def speak(self):
        print(f"{self.name} woofs!\n")


    
    def perform_trick(self, trick):
        print(f"{self.name}", end= " ") 
        match trick:
            case "sit":
                print("sits down!")
            case "lay down":
                print("lays down")
            case "stay":
                print("stays still")
            case "fetch":
                print("fectchs a ball")
            case "shake":
                print("shakes")
            case "hand stand":
                print("stands on their back paws")
            case _: 
                print("looks confused.")
            