class Budget:
    def __init__(self):
        self.expenses = {}
    
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
    
    def view_expenses(self):
        for category, amount in self.expenses.items():
            print(f'{category}: ${amount}')

budget = Budget()

while True:
    print('1. Add expense')
    print('2. View expenses')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        category = input('Enter the category: ')
        amount = float(input('Enter the amount: '))
        budget.add_expense(category, amount)
    elif choice == '2':
        budget.view_expenses()
    elif choice == '3':
        break
    else:
        print('Invalid choice. Please try again.')
