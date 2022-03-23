class Director:
    list = ['rock', 'paper', 'scissors']
# thebresponsibility of Director is to hold a list of word ['rock', 'paper', 'scissors']

    def __init__(self, artificial_player):
        self.artificial_player = artificial_player
        self.guess = ''
        self.score = 0
        

# def set_word set the initial word, to play in the game

    def set_word(self, guess):

        while(guess not in self.list):
           
            print("Choose again : {}".format(self.list))
           
            guess = input().lower()

        self.guess = guess.lower()
# def word  return the self.guess value
    def word(self):
        return self.guess


# def set_point calculate the point and stores it to be caulculated every time we play 

    def set_point(self, points):
        self.score = self.score + points
#def point returns the score
    def point(self):
        
         return(" {}\'s score is: {}".format(self.artificial_player,self.score))
