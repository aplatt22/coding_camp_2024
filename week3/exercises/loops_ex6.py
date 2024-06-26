number = input('Give me a number less than 100!\n')
number = int(number)

remainders = []

if number < 100:
    for num in range(2,number):
        remain = number % num
        remainders.append(remain)
    if 0 in remainders:
            print('That number is not prime.') 
    else:
        print('That number is prime.')     
else:
    print('the number is above 100')