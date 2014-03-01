## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is a Animal has a name
class Dog(Animal):

    def __init__(self, name):
        #define dog's name
        self.name = name

## Cat is a Animal has a name
class Cat(Animal):

    def __init__(self, name):
        ## define cat's name
        self.name = name

## Person is a object has a pet
class Person(object):

    def __init__(self, name):
        ## define person's name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person has a salary
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## define his salary
        self.salary = salary

## define a Fish object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has a pet called satan
mary.pet = satan

## frank is a Employee, his salary is 120000
frank = Employee("Frank", 120000)

## frank has a pet called rover
frank.pet = rover

## filpper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()