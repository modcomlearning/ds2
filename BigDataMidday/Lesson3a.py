
# control statements and functions
# Control Statements if, if else, elif, loops - for, while
# functions
# What is a function  -  its a block of statements/codes performing a specific task
# What else on functions? They split a large program into small pieces
# What does that help? It easy to understand your code, You can re use functions
# Functions are used in OOP.

def convert_cel_far():
    celsius = 5
    fahrenheit = celsius*9/5 + 32
    print(celsius, 'C  is equal to ', fahrenheit, 'F')
    if fahrenheit is 50:
        print('Thats okay')
    else:
        print('Thats not okay')
# trigger your function/call/used
convert_cel_far()

# convert kes to usd, euro, yen,       - 3 mins
# introduce parameters, params
def convert(kes, name): # we don't know the value of kes
    #kes = 1000
    usd = kes/108
    print(kes, 'KES = ', usd, 'USD')
    print('Your name provided was ', name)

# convert used below
convert(kes=500, name='Joe') # provide the argument to fit the paramter
convert(kes=1000, name='Ann')
convert(kes=1500, name='Greg')












