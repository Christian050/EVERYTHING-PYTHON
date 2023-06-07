has_high_income = True

has_good_credit = True

has_criminal_record = False

if has_high_income and has_good_credit:
	print('Eligible for loan')
	# Output: Eligible for loan

if has_high_income or has_good_credit:
	print('Eligible for loan')
	# Output: Eligible for loan

if has_good_credit and not has_criminal_record:
	print('Eligible for loan')
	# Output: No output

'''
Logical operators are used when there are multiple conditions.
They are written in small letters.
The logical operators are:

AND (and operator)
Both Conditions must be true.

OR (or operator)
At least one condition must be true.


NOT (not operator)
One condition must be true/false. Changes condition
from false to true and vice versa.

'''