from hilo import Hilo
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        cards (List[points]): An accumulation or deduction of instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guesser = Hilo()
        self.is_playing = True
        self.total = 300
        self.first_card = None
        self.guess = None
        self.last_card = None
        

    def random_card(self, exclusions=[]):
        """Displays the first card. Also asks the player for their guess.""" 
        choices = []
        for i in range(1,14):
            if i not in exclusions:
                choices.append(i)
        return random.choice(choices)
        """Args:
            self (Director): An instance of Director.
        """

    def start_game(self):   
        while self.is_playing:
            self.random_card()
            self.random_card([self.first_card])
            self.score()
            self.end_game()
            self.get_inputs()

    def get_inputs(self):
        play = input("Play Hilo? [y/n] ")
        self.is_playing = (play == "y")

    def score(self):    
        # Updates the player's score.
        if self.first_card > self.last_card and self.guess == 'lower':
            self.total += 100
            print("You guessed correct! You get 100 points.")
        elif self.first_card < self.last_card and self.guess == 'higher':
            self.total += 100
            print("You guessed correct! You get 100 points.")
        else:
            self.total -= 75
            print("You are incorrect... You lose 75 points.")

    def end_game(self):
        if self.score <= 0:
            self.is_playing = False 
            print("Your points are at 0.... sorry, GAME OVER!")