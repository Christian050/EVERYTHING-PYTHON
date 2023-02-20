# Create a program to translate digits into words.

user = input('Phone: ')

contact = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four', 
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
    '0' : 'Zero'
}

output = ''

for item in user:
    output += contact.get(item) + ' '
    
print(output)