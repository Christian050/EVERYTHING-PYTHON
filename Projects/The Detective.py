class Game:
    def __init__(self):
        self.location = 'home'

    def play(self):
        # while True:
        if self.location == 'home':
            print('''
                                                        CHAPTER 1
                    
                        It's the 1st of December 2018. You are home after a long semester in school 
                    filled with drama, suspense and ...murder. Can't help but wonder how gruesome
                    death could get. 'How could she die like that?' You ask yourself whilst wondering
                    who could've plotted such murder. You hear footsteps and suddenly a middle aged man
                    with black hair and a knife about to stab you. Life flashes as you get stabbed in 
                    the chest by this man and later...your're dead?
                    
                        You wake up with a start, letting out a loud scream as you grip the bed sheets
                    with wide-eyed terror. Heavy breaths from your nostrils as you realize it was a dream.
                    'You okay?' Dad asked as he heard the cry from outside, 'Yeah, just a bad dream'
                    you reply. 'You can talk to me about it' dad says with a smile on his face. 
                    'No worries, It's nothing I can't deal with' you say as you get up from bed.
                    It's a saturday, a day set aside for everyone do chores together.
                    Your mother calls out your name as you smooth out the sheet.
                    ''')
            name = input('What is your name?\n')
            if name:
                print(f'''
                      '{name}, {name}!' mom calls out. Upon hearing your name being called, you turn your head towards the source of the sound.
                      'Yes mom?' you resign with a respond, 'You slept early yesterday, don't make any excuses today', mom says, tired of your excuse of 
                      'not sleeping early' so you could skip chores and sleep all day.You begin your chores, sweeping the front porch and trimming
                      the bushes in the garden. As you work, you run into some of your friends who are also out doing their chores. "Hey, how's it going?" 
                      John greets, one of your friends. The friend group is solely made up of 7. A former bully, John, classmates Jane and Michael
                      school mates, David, Rachel and Kevin and a friend of Jane, Emma from a neighboring school.
                      "Not too bad, just trying to get this yard work done before noon," you respond, making small talk as you continue to work. 
                      Though the conversation is light and casual, you can't help but think of her death.
                      ''')
                         
                
                
                
                
                


game = Game()
game.play()