
# multiple conditions using elif
age = int(input('Whats the participant age?'))
marks = float(input('Whats the participant marks?'))

# for a child to go to the next class they need > 5 yrs, > 50 marks
# for a child to get a prize they need to be less than 5 yrs,
if age > 5 and marks > 50 :
    print('You will proceed to class 5')

elif age <= 5:
    print('They qualify for  a prize')



