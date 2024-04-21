## function
def hello(name, age=22 ):
    print(f"Hello, {name} of age {age}")

hello("Rajeeb", 24)
hello("Tom")


## Nested function
print(round(abs(float("22.3"))))


#Scope: lEGB: local, enclosing, global, builtin


## *args # if the number of argument to passed to function isnot predefined # all arguments to tuple
def multiply(*args):
    mul = 1
    for i in args:  #args is a tuple
        mul = mul * i
    return mul
print(multiply(1,2,3,4)) # can pass any argument


## **kwargs # arguments to dictionary
def hello(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,value)

hello(first="Rajeeb", last="Thapa Chhetri")


## random number
import random
random_number = random.randint(1,6) # between 1 and 6 and including 1 and 6
random_number = random.random() # from 0 to 1
random_number = random.choice([1,2,3])
list =[1,2,3] 
random.shuffle(list) # act on original
print(random_number)
print(list)

## Exception # this is good practice for try exception: first try to find specific exception as value error ...
try:
    a = 1/0
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else: # if no exceptions
    print("if no exception")
finally: # donot care about exception
    print("if will excecute irrespective of exception")