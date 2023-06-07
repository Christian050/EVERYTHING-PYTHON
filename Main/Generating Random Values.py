import random

Members = ['John', 'Christian', 'Clement', 'Bright', 'David']
Leader = random.choice(Members)
print(Leader)

for i in range(3):
    print(random.random())
    
    # Randint
    print(random.randint(10, 20))
    