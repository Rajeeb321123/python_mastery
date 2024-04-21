## inheritence

class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Hawk(Animal): # inheretance
    def fly(self):
        print("This animal can fly")


a = Hawk()
a.eat()



# Multi-level inheritance

class livingbeing:
    alive = True
class Animal(livingbeing):
    def eat(self):
        print("This animal is eating")
class Hawk(Animal):
    def fly(self):
        print("This animal is flying")

a = Hawk()
print(a.alive)



## Multiple inheretiance

class Transport:
    def move(self):
        print("this transport can move")
class Wheel:
    def rotate(self):
        print("wheel can rotate")
class Car(Transport,Wheel):
    def drive(self):
        print("Cars can be driven")

a = Car()
a.move()
a.rotate()


## Method overridding

class Animal:
    def eat(self,):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")

class Hawk:
    def eat(self):
        print("Hawk is eating")



a = Hawk()
a.eat()



## Method chaining

class Animal:
    def eat(self):
        print("Animal is eating")
        return self # must return for method chaining
    def sleep(self):
        print("Animal is sleeping")

a = Animal()
a.eat().\
    sleep()

a.eat().sleep()



## Super function

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
        
class cube(Rectangle):
    def __init__(self, length, width, breadth):
        self.breadth=breadth
        super().__init__(length=length, width=width)
    
    def volume(self):
        return self.breadth * self.length * self.width
    

a = cube(3,4,2)
print(a.area(), a.volume())




## Abstract class
from abc import ABC, abstractmethod

class Shape(ABC): # cant instaniate Shape class
    @abstractmethod
    def area(self): # this must be overridden in other child class
        pass

class Square(Shape):
    def area(self):
        return 24
    
a = Square()
print(a.area())