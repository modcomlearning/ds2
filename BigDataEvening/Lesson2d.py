
# functions  - its a block of code doing something
def grading():
    marks = float(input('What marks did you get:'))
    if marks <= 50:
        print('You Failed')  # works if condition is true

    else:
        print('You Passed')

def checker():
        age  = float(input('What is the kid age:'))
        # check if age less 8 , lower classes, else upper classes
        if age<=8:
            print('Lower classes')
        else:
            print('Upper classes')


# call/run/trigger
checker()
grading()





