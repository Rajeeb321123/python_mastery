# ## passing object as argument 

# class  Car:
#     color = None


# def change_color(car, color):
#     car.color = color

# car_1 = Car()
# change_color(car_1, "red")

# print(car_1.color)


# ## Duck typing
# ## in Python methonds, atributes of object is more import and class

# class Duck:
#     def walking(self):
#         print("Duck is walking")

# class Chicken:
#     def walking(self):
#         print("chicken is walking")

# class Person:
#     def catch(self,duck):
#         duck.walking()
#         print("Person catches it")
# duck = Duck()
# chicken = Chicken()

# a = Person()
# a.catch(chicken) # no error even we pass chicken # very simple duck name isnot cared as it just a name of arg, but attribute/ method lik .walking() is important



## Walrus operator (:=)

# print(happy := True) # True output

# foods = list()
# while food :=  input("Name the food: ").lower() != "quit":
#    foods.append(food)
# print(foods) # TRUE, True # donot use in real code # seems like no use

# a = 'Rajeeb'
# print(a.__contains__('e'))


# ## Function to vairable
# def ai():
#    print("high")

# b = ai
# b()





# ## high order function: function as argument or return function
# # 1. function as argument
# def toLower (text):
#    return text.lower()

# def b (func):
#    text = func("Hello")
#    print(text)

# hello = b(toLower)

# # 2. Return function
# def divisor(number):
#    def diveded_by(dividor):
#       return number/dividor
   
#    return diveded_by

# divide = divisor(number = 24) # number # we get divided_by function as return
# value = divide(dividor=2)
# print(value) # 12.0 



# ## lambda function
# multiply = lambda x,y : x * y  # parameter : return
# age_check = lambda age: True if age>10 else False
# print(multiply(5,2))
# print(age_check(20))


# ## sort
# a = [1, 3, 5, 2]
# a.sort(reverse=True) # sort only for list. Not for other iterable like tuple
# print(a)

# a = (1, 3, 5, 2)
# b = sorted(a, reverse=True) # return list . work for other iterable like tuple
# print(a, b)

# student = [("SpongeBob", 20), # (name, grade)
#           ("Patrick", 24)]

# student.sort() # sort by first index of tuple here name
# print(student)

# # we should make a function to return second index's value as pass that function as key
# def grades (eachRow):
#    return eachRow[1] # as grades are in second index return with index [1]
# student.sort(key=grades)
# print(student)




# ## Map function: apply function to each element of  iterable like list, tuple
# map(function, iterable)
# data = [("Car",30000),
#         ("Pencil", 1 )]
# def to_NPR(eachElement):
#    return (eachElement[0], eachElement[1]* 126)

# list_NPR = list(map(to_NPR, data) ) # return map object so we need to change it to list
# print(list_NPR)




# ## filter function: similar to js: filter function, iterable
# # fiter(function, iterable)
# data = [("Car",30000),
#         ("Pencil", 1 )]
# def filter_function(eachElement):
#    return eachElement[1] > 1000

# list_high_price_goods = list(filter(filter_function, data)) # return filter object so we need to change it to filter
# print(list_high_price_goods)



# ## Reduce function: apply reduce function on first two element and repeat process on output and next element and  until 1 value remains
# # reduce(reduce_function, iterable)
# import functools
# a = ["h", "e", "l", 'l']
# a.insert(0, "welcome to ") # for initial value like in js reduce(initial, acc, current_element) but there is no initial value in python
# def reduce_function(acc, current_element):
#     return acc + current_element
# b = functools.reduce(reduce_function, a)
# print(b)


# ## Enumerate loop
# a = [1,2,3,4,5]
# # for i in range(len(a)):
# #    print(a[i])

# #enumerate return list of tupels of (index, value)
# e = enumerate(a)
# for i in e:
#     print(i)
# print(e)

# # most imp 
# for index, value in enumerate(a):
#     print(index,value)
#     if (index>= 3):
#         print("Moving out of loop")
#         break
    

    


    


