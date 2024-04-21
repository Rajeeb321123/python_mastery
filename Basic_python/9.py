# ## list comprehension
# a = [1, 2, 3, 4, 5, 6]
# b = [ element*2 if element > 2 else None for element in a  ]
# print(b)
# c = [element for element in b if element != None ]
# print(c)


## dictionary comprehension
dic = {"Kathmandu": 20,
       "NewYork": 10,
       "LasVegas": 25}

def check(value):
    if value >= 20:
        return "Warm"
    else:
        return "Cold"
    
a = {key:(value+32) for key, value in dic.items() if value >= 20} # make a new list with only kathmandu and las Vegas
b = {key + "'s" + " Tempearture": ("Warm" if value >= 20 else "Cold") for key, value in dic.items()} # output: {'Kathmandu's Tempearture': 'Warm', 'NewYork's Tempearture': 'Cold', 'LasVegas Tempearture': 'Warm'}
c = {key + "'s" + " Tempearture": check(value) for key, value in dic.items()} # output: {'Kathmandu's Tempearture': 'Warm', 'NewYork's Tempearture': 'Warm', 'LasVegas Tempearture': 'Warm'}

print(a)
print(b)
print(c)