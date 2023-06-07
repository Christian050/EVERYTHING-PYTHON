# 2:18:30

customer = {
     'name': 'Christian',
     'age': 20,
     'is_verified': True
 }

print(customer['name'])


# Using the .get() method
print(customer.get('age'))


# Supplying default value
print(customer.get('birthday', '31st December 2002'))


# Updating dictionary
customer['name'] = 'Jamie Fox'
print(customer['name'])


# Adding key
customer['year'] = 2022
print(customer['year'])


'''
A dictionary is used to store information in key value pairs
and are written in curly braces(brackets)'{}'.

You cant repeat the same keys in a dictionary and can contain anything
and returns a KeyError when:

1, The key isn't the same as the one in the dictionary (Case Sensitive).

2, If the key isn't in the dictionary (Unavailable).

None is returned instead of KeyError when the .get() method is used and the key is not available.
It represents the absence of a value.

A default value can be specified to a dictionary using the .get() method.
'''