
# Operators, Control statements
# Operators: Arithmetic +, -, /, *, %,
# Operators: Comparison: > , < , >=, <=, ==, !=
# Operators: Logical : and, or , not
# Operators: Membership: in , not in
# Operators: Identity:  is , is not

time = 24
principle = 60000
rate = 1.5
name = 'Kelvin'

interest = principle * rate *time/112
print('Your Name: ', name)
print('Your Interest ', interest, 'KES')

formatted_float = "{:.3f}".format(interest)
print(formatted_float)
# Comparison Operators, constrol statements
if time <= 12:
    print('You will get 5% relief')  # works if its true

elif time <=24:
    print('You will get 10% relief')

elif time <=48:
    print('You will get 15% relief')
    








