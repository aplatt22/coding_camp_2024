def is_prime(number):
    remainders = []
    for num in range (2,number):
        remain = number % num
        remainders.append(remain)
        if remain == 0:
            break
    if 0 in remainders:
        return False
    else:
        return True    
    
number = input('Give me a number less than 100!\n')
number = int(number) 

trials = 0
tested_numbers = []

while number < 100:
    if is_prime(number):
        print('That number is prime!')
        break
    else:
        # print('That number is not prime.')
        trials +=1
        if number in tested_numbers:
            print('You have to be kidding me, you already tried this one! Stop wasting my time.')
            number = int(input("Give me another number you haven't already tried.\n"))
        elif trials in [1, 2]:
            number = int(input("Prime numbers are hard, try again and you'll get it!.\n"))
        elif trials >= 3:
            number = int(input('A monkey could find a prime number sooner, try again dummy.\n'))
        tested_numbers.append(number)
        
else:
    print('The number is above 100, run the program again and do better.')