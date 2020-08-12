
print(2000)
print(3000)
print('I love big data')

# Variables - they store values in memory
# data types: int, float, list, tuple, dictionary, string
number = 45 # int
age = 10 # int
score = 500 # int
points = 56 # int

weight = 70.5 # float
height = 1.4 # float

name = 'Joseph' # strings,
school = 'Modcom' # strin

print(number)
print(weight)
print(school)

# list - stores many values in a single variable
shopping_list = ['Bread','Salt','Airtime','Sugar']
print(shopping_list)

tokens = [45,23,56,78,78.5,78,56,89]
print(tokens)
print(shopping_list[3]) # get items by index
print(tokens[6])

# tuple - stores many values in a single variable
best_teams = ('Man U','Arsenal','Chelsea','Liverpool')
print(best_teams)

marks = (56, 78, 89.5, 45, 20, 78, 56.5)
print(marks)

print(best_teams[2]) # chelsea
print(best_teams[1:3])  # Always a -1


# What is difference between a list/tuple?
# List is mutable - update
shopping_list.append('Soap')
shopping_list.remove('Salt')
shopping_list.insert(3, 'Cake')
print(shopping_list)

# tuple are immutable- cannot be updated
print(type(best_teams))












