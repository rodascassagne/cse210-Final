
class Director:

    list = ['rock', 'paper', 'scissors']
    
# thebresponsibility of Director is to hold a list of word ['rock', 'paper', 'scissors']

    def __init__(self, x1):
        
        self.artificial_player = x1
        self.guess = ''
        self.score = 0
        

# def set_word set the initial word, to play in the game

    def set_word(self, y):

        while(y not in self.list):
           
            print("Choose again : {}".format(self.list))
           
            y = input().lower()   # ESTO ES PARA RESETEAR Y VOLVER A HACER LA PREGUNTA

        self.guess = y.lower()
# def word  return the self.guess value
    def word(self):
        return self.guess


# def set_point calculate the point and stores it to be caulculated every time we play 

    def set_point(self, points):
        self.score = self.score + points
#def point returns the score
    def point(self):
        
         return(" {}\'s score is: {}".format(self.artificial_player,self.score))
    


  
