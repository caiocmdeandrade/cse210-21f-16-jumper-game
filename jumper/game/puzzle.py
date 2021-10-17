import random

class Puzzle:
    """A code template for our hider. The responsibility of this class of
    objects is to watch the seeker and give hints.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the hider (1-1000).
        distance (list): The distance from the seeker.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        """
        self.word = list("house")
        #self.word = self.choose_a_word()
        self.draws = ["   ___", "  /   \\", " /_____\\", " \     /", "  \   /", "   \ /", "    0", "   /|\\", "   / \\", " ^^^^^^^"]
        self.guessed_letters = {}



    def choose_a_word(self):
        words = ["book", "house", "mouse"]
        word = list(random.choice(words))
        return word    


    def compare(self, guess):
        """Keeps track of how far away the seeker is by calculating the difference
        between their locations. The distance is appended to the corresponding attribute for later use.

        Args:
            self (Hider): An instance of Hider.
            location (number): An whole number that is passed internally
        """
    
        for i in range(len(self.word)):
            letter_index = i
            letter = self.word[i]
            if (guess == letter):
                self.guessed_letters[letter_index] = letter


    def draw_pic(self):
        for i in self.draws:
            print(i)        


    def get_hint(self):
        """Returns a hint that depends on whether or not the seeker has moved
        closer or farther away. This is determined by inspecting the last two distances contained
        in the distance attribute.

        Args:
            self (Hider): An instance of puzzle.
        
        Returns:
            string: A response for the player.
        """
        
        # La cantidad de elementos de la lista es igual a la del diccionario
        if (len(self.word)) == (len(self.guessed_letters)): 
            response = "\nCongratulations!! You discovered the word!!"
        
        else:
            response = "Keep trying but try to loose not your head!!"

        return response

    