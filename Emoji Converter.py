# 2:26:30

message = input('> ')
words = message.split(' ')

emoji = {
    
    ':)' : '😊',
    ':(' : '😔',
    ';)' : '😉',
    '-.-': '😑',
    ':3' : '😙',
    ':>' : '😁',
    ':0' : '😮',
    ':o' : '😮‍💨',
    'XD' : '🤣',
    'xo' : '💀', 
    ':p' : '😛', 
    ';p' : '😜', 
    'xp' : '😝', 
    ':/' : '😕',
    ":|" : '😐',
    '¦|' : '😑'
    
}

output = ''

for word in words:
    output += emoji.get(word, word) + ' '

print(output)



'''
The .split method breaks down sentences into words.

The data in the brackets isn the separator,
.ie where the sentence splits/breaks.

Provides output in list format.
'''