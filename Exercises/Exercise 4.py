'''
Price of a house is $1M.
If the buyer has good credit, 
they need to put down 10%
otherwise they need to put 
down 20%.
Print the down payment.

'''

price = 1000000
good_credit = True

if good_credit:
	down_payment = 0.1 * price
else:
	down_payment = 0.2 * price

print(down_payment)



# OR




price = 1000000
has_good_credit = True

if has_good_credit:
	down_payment = 0.1 * price
else:
	down_payment = 0.2 * price

print(f'Your down payment is ${down_payment}')