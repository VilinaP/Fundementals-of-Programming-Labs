print('Please enter the quantity for each of the indicated denominations.')

bills20 = int(input('Twenty dollar bills:'))
bills10 = int(input('Ten dollar bills:')) 
bills5 = int(input('Five dollar bills:'))
bills1 = int(input('One dollar bills:'))
cents25 = int(input('Quarters:'))
cents10 = int(input('Dimes:'))
cents5 = int(input('Nickles:'))
cents1 = int(input('Pennies:'))

print('Cash entered: $'+ str(f'{(bills20*20 + bills10*10 + bills5*5 + bills1*1 + cents25*0.25 + cents10*0.10 + cents5*0.05 + cents1*0.01):.2f}'))

