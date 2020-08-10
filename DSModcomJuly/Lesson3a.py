
# elif is used for multiple condition
marks = float(input('What did you get last time?:'))
print('Marks entered: ', marks)

# elif is an improvement of if else
if 0  < marks < 30:  #  0  < marks < 30
    print('You Failed')

elif 30 < marks <=50:  # 30 < marks <=50
    print('You have an Average')



elif marks > 50 and marks <=75:  # 50 < marks <=75
    print('You got Above average')

elif marks > 75 and marks <=100:  # 75 < marks <=100
    print('Excellent!')

# any other, over 100 or less than 0
else:
    print('Your marks should be btwn 0 - 100, Retry!')
