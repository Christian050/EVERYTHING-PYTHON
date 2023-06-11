# A python code to accept 3 numbers and arrange them in ascending order

user_input_1 = float(input('Enter first number\n'))
user_input_2 = float(input('Enter second number\n'))
user_input_3 = float(input('Enter third number\n'))

List = [user_input_1, user_input_2, user_input_3]
List.sort()
print(List)

a = int(input("a:\t"))
b = int(input("b:\t"))
c = int(input("c:\t"))

if (a <= b) and (b <= c):
    print(a, b, c)
elif(a < c) and (c <= b):
    print(a, c, b)
if (b < a) and (a <= c):
    print(b, a, c)
elif (b < c) and (c <= a):
    print(b, c, a)
if (c < a) and (a <= b):
    print(c, a, b)
elif (c < b) and (b <= a):
    print(c, b, a)