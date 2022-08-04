import random

#https://youtu.be/XKHEtdqhLK8?list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&t=11669

''' #방법1
choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = input("rock, paper, or scissors? : ")

print('computer : ', computer)
print('player : '+player)
'''


#방법2


while True : 
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? : ").lower()

    if player == computer:
        print('computer : ', computer)
        print('player : '+player)
        print('Tie!')
    elif player == 'rock':
        if computer == "paper":
            print('computer : ', computer)
            print('player : '+player)
            print('You lose')
        if computer == 'scissors':
            print('computer : ', computer)
            print('player : '+player)
            print('You win!')
    elif player == 'scissors':
        if computer == "rock":
            print('computer : ', computer)
            print('player : '+player)
            print('You lose')
        if computer == 'paper':
            print('computer : ', computer)
            print('player : '+player)
            print('You win!')
    elif player == 'paper':
        if computer == "scissors":
            print('computer : ', computer)
            print('player : '+player)
            print('You lose')
        if computer == 'rock':
            print('computer : ', computer)
            print('player : '+player)
            print('You win!')
    play_again = input("play again? (Y / N) : ").lower()
    
    if play_again != 'y':
        break
print('bye~~')