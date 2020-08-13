
# a block of code doing something
def westlands():
    marks = float(input('What did you get?'))

    if marks <= 50:
        print('You Failed')  # will run if condition is true

    else:
        print('You Passed')  # will run if condition is false


def eastlands():
    age = int(input('Whats the participant age?'))
    marks = float(input('Whats the participant marks?'))
    # for a child to go to the next class they need > 5 yrs, > 50 marks
    # for a child to get a prize they need to be less than 5 yrs,
    if age > 5 and marks > 50:
        print('You will proceed to class 5')

    elif age > 0 and age <= 5:
        print('They qualify for  a prize')

    elif age > 5 and marks <= 50:
        print('You will not proceed to the next class')

    else:
        print('Please check your inputs')


# which function are you running
def kenya():
    temp = int(input('Enter Temp'))
    if temp > 36.1 and temp < 37.5:
        print('Normal')

# you have to call the function
kenya()
