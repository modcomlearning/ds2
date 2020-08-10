
# nested statements
# as if statements inside another if statements
age = int(input('What is your age?:'))
weight = float(input(' What is your weight(Kgs): '))

print('Age entered: ', age, 'Weight entered: ', weight)
# someone can donate blood,, less than 50kgs you can't donate
# Less than 18 year cannot donate.

if age >=18:
    if weight <=50:
        print('You cant donate ')  # less than 50 kgs
        if weight > 45:
            print('We can consider')
        elif weight > 40 and weight < 45:
            print('we can somehow consider')
        else:
            print('We cant consider')
    else:
        print('You can donate') # more than 50kgs

else:
    print('You cant donate')  # less than 18
    if weight > 60:
        print('We can consider')

#  0729 225 710
# check google classroom for more





