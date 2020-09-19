print(1000)

# variables - store values
# Data types: int(whole numbers), float(decimals), string(xters),lists, tuples, dictionaries
temp = 36.5  # float
height = 1.5 # float

age = 20  # int
marks = 56 # int

print(temp)
print(height)
print(age)
print(marks)

name = 'Joseph Modcom' # string
print(name)

# tuple store many values in one variable
points = (78,78,55,66,22,77,88,55,11,22,55,66,78,99,78.9,'Ann')  # tuple/array
print(points)
print(points[2])

total = points[0] + points[4]
print(total)

counties = ('Embu','Kisumu','Nairobi','Nandi','Kajiado','Nakuru','Meru')
print(counties)
print(counties[0:4])  # slicing a tuple
print(counties[2:5])

# Lists store many values in one variables
teams = ['Man U','Chelsea','Liverpool','Man City']
scores = [2,5,5,2,2,3]
print('I support', teams[2], 'Because they scored ', teams[1], scores[1],' Goals')
print(teams[0:2]) # slicing a list

# Lists vs tuples in terms functionality
# Lists are mutable(updated)
# tuples are immutable(cannot be updated)
teams.append('PSG')
teams.remove('Liverpool')
print(teams)








