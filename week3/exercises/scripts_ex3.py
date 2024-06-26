price = float(input('What was the price?\n'))
tip = float(input('What percentage would you like to tip?\n'))

tip_percent = tip/100

tip_amount = (price * tip_percent)

total = price + tip_amount

print(f'Your total cost is ${total:.2f}')