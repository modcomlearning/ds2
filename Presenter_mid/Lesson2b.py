
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
    height = 1.6 # m
    weight = 60.5 # kgs
    bmi = weight/(height*height)
    print('Your BMI is ', bmi)
    # Control statements
    # Comparison operators: > , >=, <, <=, ==, != (Not equal)
    # Logical Operators: and, or, not
    # use if, if else, elif
    if bmi < 18.5:
        print('Underweight')
        answer = bmi/89
        print(answer)

    elif bmi >= 18.5 and bmi <= 24.9:
        print('Normal')

    elif bmi >= 25 and bmi <=29.9:
        print('Overweight')

    elif bmi >=30 and bmi <=100:
        print('Very Overweight')

    else:
        print('Invalid BMI')  # out of our conditions


body_mass_index()


