# Weight = input('Weight: ')
# Unit = input('(L)bs or (K)g: ')

# if Unit.upper() == 'L':

# 	product = int(Weight) * 0.45
# 	print(f"You weigh {product} pounds.")

# elif Unit.upper() == 'K':

# 	product = int(Weight)  / 0.45
# 	print(f"You weigh {product} kilograms.")

# else:
# 	print('Enter the correct Unit')




weight = input('Weight: ')

if weight.isnumeric():
	unit = input('(L)bs or (K)g: ')

	if unit == 'L':
		product = int(weight) * 0.45
		print(f"You weigh {product} pounds.")

	elif unit == 'K':
		product = int(weight) // 0.45
		print(f'You weigh {product} kilos.')

else:
		print('Enter the correct unit.')