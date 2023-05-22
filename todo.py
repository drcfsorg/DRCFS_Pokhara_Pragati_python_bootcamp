fruits = ['apple', 'mango', 'orange', 'banana']

print(type(fruits))

# indexing: selecting (taking out) an item from the data. In indexing,
# python always starts from 0. That means, the first item can be accessed
# from 0 and not 1.

# Indexing can be done by: variable_name[n]    -> where n is a number 


print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


# negative indexing starts with variable_name[-n] where n is the length of number 


print(len(fruits)) # displays length of fruits

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])


for item in fruits:
    print(f"name of the fruit is {item}")  


"""
for index in range(len(fruits)):
    name = fruits[index]
    print(name)
"""

# using while loop
i = 0
while i < len(fruits):    # while i is less than length of item in fruits

    print(fruits[i])
    i = i + 1
