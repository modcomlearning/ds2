
# functions and control statements
# function = its a block of code performing some related tasks
# Advantages of functions - makes you code simple/easy to understand
# Make your code easy to maintain
# Functions makes it easier to work with OOP
# We do a function to find SI
def simple_interest():
    principle = 60000
    rate = 7.9
    time = 24
    yourname = 'Joe'

    # arithmetic operators   +, -,/,*, %(Modulus)  2%2 = 0
    answer = (principle * rate * time)/100
    print('Your SImple Interest is ', answer)


simple_interest()  # a function call/run/invoke

def body_mass_index():
    height = 1.6
    weight = 75.5
    bmi = weight/(height*height) * 703
    print('Your BMI is ', bmi)


body_mass_index()



