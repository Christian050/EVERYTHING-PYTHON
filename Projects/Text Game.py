class Game:
    def __init__(self):
        self.location = 'home'

    def play(self):
        while True:
            if self.location == 'home':
                print('You are at home.')
                print('What do you want to do?')
                print('1. Go to the park')
                print('2. Go to the store')
                print('3. Quit')
                choice = input('Enter your choice: ')
                if choice == '1':
                    self.location = 'park'
                elif choice == '2':
                    self.location = 'store'
                elif choice == '3':
                    break
                else:
                    print('Invalid choice. Please try again.')
            elif self.location == 'park':
                print('You are at the park.')
                print('What do you want to do?')
                print('1. Play on the playground')
                print('2. Go for a walk')
                print('3. Go home')
                choice = input('Enter your choice: ')
                if choice == '1':
                    print('You play on the playground.')
                elif choice == '2':
                    print('You go for a walk.')
                elif choice == '3':
                    self.location = 'home'
                else:
                    print('Invalid choice. Please try again.')
            elif self.location == 'store':
                print('You are at the store.')
                print('What do you want to do?')
                print('1. Buy groceries')
                print('2. Browse the electronics')
                print('3. Go home')
                choice = input('Enter your choice: ')
                if choice == '1':
                    print('You buy some groceries.')
                elif choice == '2':
                    print('You browse the electronics.')
                elif choice == '3':
                    self.location = 'home'
                else:
                    print('Invalid choice. Please try again.')

game = Game()
game.play()
