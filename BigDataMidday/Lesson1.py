
print(8000)
print('Hello Python')
# variables and datatypes
# variables store data using a specific data type
# 6 different data types
# int, floats, string, list, tuples, dictionaries
pin_number = 56565  # int
weight  = 80.5  # float
name = 'Joseph Modcom'  # string

print(pin_number)
print(weight)
print(name)

# lists - store many values at once in one variable
ages = [9,3,5,3,5,4,6,4,6,7,5,4,3,6,4,6,4,6,4,6,4,6.5]
print(ages)

kids_names = ['Ali','Ken','Mary','Ann','Joseph','Clare',7000]
print(kids_names)

# slicing
print('The child name is ', kids_names[4], 'Her age is ', ages[8])

# tuples  - store many values at once in one variable
points = (5000,7000,5000,3000,5000,8000,9000.6)
print(points)

prizes = ('Phone','Tv Set','Camera')
print(prizes)

# slicing
print('I got', points[1], 'Points, I took home a', prizes[2])

# Difference between a list and a tuple
# tuple is immutable/can't be updated at runtime
# list is mutable/updated at runtime
ages.append(11)
kids_names.append('Irene')
kids_names.remove('Ann')

print(kids_names)
print(ages)






