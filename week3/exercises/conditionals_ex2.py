number = input('What number would you like to learn about?\n')
number = int(number)

if number % 2 == 0:
    if number <= 7:
        print('The number is divisible by 2!')
    elif number > 7:
        print('The number is divisible by 2!')
        print(f'The remainder of dividing by 7 is {number % 7}!')
elif number % 3 == 0:
    if number <= 7:
        print('The number is divisible by 3!')
    elif number > 7:
        print('The number is divisible by 3!')
        print(f'The remainder of dividing by 7 is {number % 7}!')
else:
    if number > 7:
        print(f'The remainder of dividing by 7 is {number % 7}!')