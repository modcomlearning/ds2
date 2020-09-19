# functions and control statements
# A functions is a block of statements performing specific task
# Advantages: makes easy to understand and maintain, used OOP, improve code reuse.
def simple_interest():
    principle = 7000
    rate = 2.5
    time = 24
    answer = (principle * rate * time)/100
    print('Your Simple interest is: ', answer)
simple_interest()   # call/use


def body_mass_index():
    weight =  float(input('What is your Weight in Kgs'))
    height = float(input('What is your Height in m'))

    bmi = weight/(height*height)
    print('Your Body Mass Index is ', bmi)
    # Comparison operators: >, >=, <, <=, ==, !=(Not equal to)
    # Logical operators: and, or, not
    if bmi < 18.5:
        print('Underweight')

    elif bmi >= 18.5 and bmi <= 24.9:
        print('Normal')

    elif  bmi > 24.9 and bmi <= 29.9:
        print('Overweight')

    else:
        print('Very Overweight')


body_mass_index()














