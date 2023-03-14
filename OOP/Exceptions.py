try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')


'''
exit code 0
Code run successfully with no errors.


Value Error(Exception)

invalid literal for int() with base 10: '[insert_string_here] (exit code 1)
String does not contain a valid code number that can be converted to an integer.

try except is used to handle errors.
'''