
tuple = ('Red','Blue','Green')
list = ['Beta','Alpha','Omega']

print(tuple)
print(list)
print(tuple[2])

# Lists(mutable - updated) vs tuple(immutable - cant updated)
list.append("Theta")
list.append("Delta")
list.remove("Beta")

print(list)
