import random

# TODO: Implement the Die class as follows...
# 1) Add the class declaration. Use the following class comment.
#A small cube with a different number of spots on each of its six sides.

class Hilo:
# 2) Create the class constructor. Use the following method comment.
    #Constructs a new instance of cards with a value and points attribute between 1-13.
    def __init__(self):#Args:self (hilo): An instance of hilo.            
    #Attributes:
    
        self.first_card = None
    
# 3) Create the (self) method. Use the following method comment.
    #imports a new random card and then asks the player if they guess "high" or "low"
def guess(self):
    # The responsibility of the guesser is to determine if the last_card is higher or lower and input that data 
        self.random_card = self.first_card  
        guesser=input("Do you guess the last card to be higher or lower? h/l")
        self.random_card = self.last_card
        return 