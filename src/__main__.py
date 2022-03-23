from director import Director
from score import Score

# the respomsibility of check_result is to calculate and compare
#  the word we write versus the word that is in the computer 

def check_result(player, artificial):

    if player.word() == artificial.word():
        print('Both guessed the same!')
        player.set_point(0.5)
        artificial.set_point(0.5)
        
    elif player.word() == "scissors":
        if artificial.word() == "paper":
            print("You win! Scissors cuts paper!")
            player.set_point(1)
        else:
            print("You lose. Rock smashes scissors! ")
            artificial.set_point(1)

    elif player.word() == "paper":
        if artificial.word() == "rock":
            print("You win! Paper covers rock! ")
            player.set_point(1)
        else:
            print("You lose. Scissors cuts paper! ")
            artificial.set_point(1)

    elif player.word() == "rock":
        if artificial.word() == "scissors":
            print("You win! Rock smashes scissors! ")
            player.set_point(1)
        else:
            print("You lose. Paper covers rock! ")
            artificial.set_point(1)

artificial = Score()
player = Director(input('\nWhat is ypour name?: '))

while True:
    print('Make a guess!: (rock, paper, scissors)')
    player.set_word(input())
    check_result(player, artificial)
    print(f'{player.point()} ')
    print(f'{artificial.point()}')
    print('\n')
    

    

