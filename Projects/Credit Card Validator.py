'''
Remove any '-' or ' '
Add all digits in the odd places from right to left
Double every second digit from right to left.
    (if  result is a two digit number,
    add the two digit number to get a single digit)
Sum the total of steps 2 & 3
If sum is divisible by 10, the credit card  number is valid

'''

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
# Accept credit card number
card_number = input('Enter a credit card #: ')

# Remove separators
card_number = card_number.replace('-', '')
card_number = card_number.replace(' ', '')

# Sum digits from right to left
card_number = card_number[::-1]

# Step 2
# Add all digits in odd places from right to left
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
# Double every second digit from right to left
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 +(x % 10))
    else:
        sum_even_digits += x 
        
# Step 4
# Add both sum of odd digits and sum of even digits
total = sum_odd_digits + sum_even_digits


# Step 5
# Check if divisible by 10
if total % 10 == 0:
    print('The Credit Card is Valid.')
else:
    print('The Credit Card is Invalid.')
