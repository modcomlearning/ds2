
print(20000)
print(5000)
print('I Love Big data')

# lets look at variables, data type
# 5 data types: int, float, lists, tuple, dictionaries, string
number = 10    # int
age = 56       # int
money = 200.5   # float
weight = 75.8   # float

print(number)
print(age)
print(money)
print(weight)

# list   - uses []
marks = [36,25,56,78,89,78,89,78,23,45,45.6]
print(marks)

counties =['Bomet','Nakuru','Nairobi','Kisumu']
print(counties)

print(marks[5])
print(counties[1])

# tuple - uses ()
tokens = (4555,8888,8889,2333,4444,8844)
teams = ('Chelsea','Man U',"Arsenal",'Man City','Liverpool')

print(tokens[0])
print(teams)

# What is the difference between a list and a tuple
# lists can be updated/mutable
counties.append('Nyeri')
counties.remove('Kisumu')
print(counties)

# tuples cannot be updated/immutable

name = 'Joseph' # string
# ALways remember to check the type of your variables


# code : w7ilgll

person = {'name': 'Joseph', 'age':20}
print(type(person))

person['weight']  = 70 # adding
person['age']  = 30 # updating

person.pop('name')

#person.clear()
# del person

print(person)

























