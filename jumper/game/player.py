import random

class Player:
    """A code template for a the seeker who looks for the hider. The 
    responsibility of this class of objects is to move from location to 
    location in pursuit of the Hider.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Seeker (1-1000).
        distance (list): The distance travelled with each move.
    """

#
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self.mentioned_letters = []
         
    def choose_letter(self, guess):
        guess = guess.lower()
        while True:
            if ((len(guess) == 1) and (guess.isalpha()) and (guess not in self.mentioned_letters)):
                self.mentioned_letters.append(guess)
                break
            else:
                print("Remember you must type one letter and it needs to be a different one than: " + ", ".join(self.mentioned_letters))
        return guess


    def get_message(self, p_word, guess):
        """Gets a message from the seeker.

        Args:
            self (Seeker): An instance of Seeker.
        
        Returns:
            string: A message from the seeker.
        """
        message = "\nI'm going to discover the word!"

        
        

        #if len(self.guessed_letters) > prev_len



        if self.gu[-1] == 0:
            message = "\nI'm going to find you!"
        elif self.distance[-1] < self.distance[-2]:
            message = "\nShhh. I'm sneaking in now..."
        elif self.distance[-1] > self.distance[-2]:
            message = "\nI'm running around, but I'll find you..."
        return message