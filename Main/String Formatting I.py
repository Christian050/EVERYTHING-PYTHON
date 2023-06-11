# Create an empty list. Append 4 strings to the list, then pop one item off at the end of the list
a = []
a.append('aaa')
a.append('bbb')
a.append('ccc')
a.append('ddd')
a.pop()
print(a)


# Use the "for" statement to print the items in the list
for item in a:
    print(item)

# Use the string "join" operation to concatenate the items in the list
e ='||'.join(a)
print(e)

# Use lists containing three (3) elements to create and show a tree
b = ['bb', None, None]
c =['cc', None, None]
root = ["aa", b, c]

def show_tree(t):
    if not t:
        return
    print(t[0])
    show_tree(t[1])
    show_tree(t[2])

show_tree(root)