number = int(input('400'))
# number greater than 100 and less than 500
while number < 100 or number > 500:
    print('Incorrect number, Please enter correct number:')
    number = int(input('400'))
else:
    print("Given Number is correct", number)
