import sys
print(sys.version)


## Type casting
a = 1
print(type(str(a)))
print(float(a))
print(int(a))

## Multiple assignment
a,b,c = "1", 2, 3.0
print(a,b,c)
a=b=c=30
print(a,b,c)

## String methods
name = "rajeeb"
print(name.find("j")) # return the first index
print(name.capitalize()) # first letter
print(name.lower())
print(name.upper())
print(name.isdigit())
print(name.isalpha()) # any symbol and digit: false
print(name.count("e"))
print(name.replace("e","x"))
print(name*3)
print(name)

## Input
# name = input("What's your name: ")
# age = int(input("What's your age: "))
# height = float(input("What's your height: "))
# print("My name is " + name +" and my age is " + str(age) + " and my height is " + str(height) ) # concatenation need same data 

## Math functions
import math
pi = 3.14
print(round(pi))
print(math.ceil(pi)) # to next high number here 4
print(math.floor(pi)) # to next low number
print(abs(pi))
print(pow(pi, 2)) # pi^2
print(math.sqrt(pi))
print(max(1,2,3,4))
print(min([1,2,3,4,5]))