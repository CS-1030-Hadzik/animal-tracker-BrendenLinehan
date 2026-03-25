from animal import Animal
from dog import Dog
from cat import Cat

if __name__ == "__main__":
    #object of the animal class. Or instance of the animal class
    animal1 = Animal("Gus", "Mouse")
    dog2= Dog("Nala", "Canine", "Medium")
    cat1 = Cat("Henry", "Cat", "Orange")

    print(animal1)
    animal1.speak()

    print(dog2)
    dog2.speak()

    print(cat1)
    cat1.speak()


    # TODO print out all the animals
