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

while number < 100:
    if is_prime(number):
        print('That number is prime!')
        break
    else:
        print('That number is not prime.')
        number = int(input('Provide another number.\n'))
else:
    print('The number is above 100, run the program again and do better.')