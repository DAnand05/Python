'''Q1. Create a class student and object itself also make it function name talk (talk: use for print
student details)'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def talk(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


# Creating an object of the Student class
student1 = Student("John Doe", 17, "11th")

# Calling the talk method to print the student's details
student1.talk()


'''Q2. Explain types of Inheritance in python with example.'''

'''Single Inheritance:
Single inheritance involves creating a new class that inherits the attributes and methods of a single base class.'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Dog barks.")


dog = Dog("Buddy")
dog.speak()

'''Multiple Inheritance:
Multiple inheritance allows a class to inherit attributes and methods from multiple base classes.'''
class Flyable:
    def fly(self):
        print("Flying.")


class Swimmable:
    def swim(self):
        print("Swimming.")


class FlyingFish(Flyable, Swimmable):
    pass


fish = FlyingFish()
fish.fly()
fish.swim()

'''Multilevel Inheritance:
Multilevel inheritance involves creating a chain of inheritance where one class inherits from another, and then a third class inherits from the second class, and so on.'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Dog barks.")


class Bulldog(Dog):
    pass


bulldog = Bulldog("Bruno")
bulldog.speak()

'''Q3.  Explain the super keyword with example'''

'''In Python, the super() keyword is used to call a method or attribute from a parent class. 
It's commonly used in class inheritance to access the methods and attributes of the parent class.

Here's an example to illustrate how super() works:'''
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        super().make_sound()
        print("And wags its tail.")


dog = Dog("Buddy", "Woof")
dog.make_sound()
