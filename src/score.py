from director import Director
import random
#Scores class gets a ramdon word betweeh thr list file ['rock', 'paper', 'scissors'], it have to be #before we type a word, them it is stores in a variale guess, to later play with the real player
class Score(Director):
    def __init__(self):
        self.artificial_player = 'artificial_player'
        self.guess = ''
        self.score = 0
        
#get_word  return the ramdpn word selected
    def word(self):
        return random.choice(self.list)
