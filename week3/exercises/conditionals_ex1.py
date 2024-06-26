life_gave = input('What has life given you?\n')

if 'lemon' in life_gave:
    print('You should make lemonade!')
elif 'orange' in life_gave:
    print('You should make orange juice!')
elif life_gave == 'money':
    print('You should buy lemons or oranges to make lemonade or orange juice!')
elif life_gave == 'love':
    print('Love is not an item you fool!')
else:
    print('How am I supposed to know what you should do?')
