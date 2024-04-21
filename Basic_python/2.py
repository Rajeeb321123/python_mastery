## String slicing
# String slicing: create as substring - by extracting element from another string
#                 indexing[] or slicing()
#                 [strat: stop: step]
# a = "012345678"

# print(a[3])
# print(a[3:])
# print(a[:3])
# print(a[3:8])
# print(a[-4:])
# print(a[:-1])
# print(a[-1])
# print(a[3:8:2]) # take  2 setps
# print(a[3:7:2]) # take  2 setps
# print(a[::2]) # take  2 setps
# reversed_a = a[::-1] # reversing with the help of slicing
# print(reversed_a)
# print(reversed_a[0:5:1])
# website_google = "http://google.com"
# website_tensorflow = "http://tensorflow.com"
# slice = slice(7,-4)
# print(website_google[slice])
# print(website_tensorflow[slice])

### if: if - elif - else - ":"
### logical operator => and: and, or: or & not: not(a >= 20), not(a >= 20 and a<= 40)

### While loop:
# i = 0
# while i < 3:
#     print("Inside while")
#     i +=1
    
# name = ""
# while (len(name)==0):
#     name = input("What is your name: ")
# print("My name is " , name)
# name = None
# while not(name):
#     name = input("What is your name: ")
# print("My name is " , name)

### For loop:
# range(start, stop, step)
# for i in range(3):
#     print(i)
# for i in range (3, 6):
#     print(i)
# for i in range(6, 12, 2): # taking 2 step each time
#     print(i)
# for i in "Rajeeb":
#     print(i)
# import time
# for seconds in range(3, 0, -1): # start from 10 to 0 in reverse order
#     print(seconds)
#     time.sleep(1) # sleep for 2 sec
# print("Happy Birthday")

# ## Nested loop
# for i in range(3):
#     for j in range(3):
#         print("a",end=" ") # end = ' ' means at the no new line but ' ' (space here)
#     print("b")

# for i in "+977-9869-361432":
#     if(i == "+" or i == "-"):
#         continue
#     print( i, end ="" )
# print("\n")
# for i in range(1,5):
#     if i == 2:
#         pass # doesnot do anything, not necessarily used often as it's logic can be done with writing it at all
#     else:
#         print(str(i), end="")

## list 
# a = [1,2,"tom",4,"John"]
# a.append("harry")
# a.pop()
# a.insert(1,"Cena") # insert at givern index and shift other to right
# a.remove("tom")
# a=[1,4,2,5,3]
# a=["Tom","Adam johnson", "Xeria"] # according to first alphabet letter, case sensitive capital always comes first than the word with small letter at top
# a.sort()
# print(a)
# print(a.count("Tom"))
# print(a.index("Xeria"))
# a.clear()


# ## 2D list
# a = [1,2,3,4,5]
# b = [6,7,8]
# c = [9,10,11]

# twod_array = [a, b, c]
# print(twod_array)
# print(twod_array[1])
# print(twod_array[0][0:-3])

# ## Tuple # ordered and unchangable # ordered means while printing with for loop order will be same as while we created them
# a = ("bro", 24, "code")
# print(a.count("bro"))
# print(a.index("bro"))
# print(a[1])

# if "bro" in  a:
#     print("bro is inside a")

# ## set # unordered, unindexable, no duplicate value
# a = {"tom","harry", "Qui", "adam","adam","adam"}
# a.add("jerry")
# a.remove("Qui")
# b = {"John", "Rajeeb", "Rama"}
# new_set_c = a.union(b) # create a new set by join  two set without touching prev sets
# print(a.difference(b)) # what a has that b doesnot
# print(a.intersection(b)) # what a has and b also
# print(a) # no duplication
# a.update(b) # add one set to another
# print(a)
# for i in a:
#     print(i) # not same order as we created them
# if "harry" in a:
#     print("harry in a")
# a.clear()
# print(a)


# ## Dictionary # key value pair
# capitals = {"USA": "Washington DC",
#             "Nepal": "Kathmandu",
#             "Mars": "Olympus"}

# print(capitals)
# print(capitals["Nepal"]) # unsafe way to get value from key # error if no key
# print(capitals.get("Nepal")) # safe way # no error if no such key in dictionary
# print(capitals.get("Bhutan"))
# print(capitals.keys()) # this isnot list, not iterable
# print(list(capitals.keys())) # Now this is a list
# print(capitals.values())
# print(capitals.items())

# for keys, values in capitals.items():
#     print(keys, values)

# capitals.update({"Germany":"Berlin"}) # add new
# print(capitals)
# capitals.update({"USA":"Dallas"}) # change the existing
# print(capitals)
# capitals["USA"] = "NewYork" # change the existing
# print(capitals)
# a = capitals.pop("Nepal")
# print(capitals)
# print(a)
# capitals.clear()
# print(capitals)


# "aaa".islower()
# "aaa".isupper()
# "aaa".upper()
# "aaa".lower()
# "aaa".capitalize()
