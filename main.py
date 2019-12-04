# Hangman game
# Import Hangman class

from Hangman import Hangman

# Ask user if they want to play the game.
print("Welcome to Hangman!\n")
# Assign the response to a variable.
play = input("Would you like to play a game? (y/N) ")
# Convert the response to lower case and if it is not "y", exit program.
if play.lower() != "y":
    print("Maybe later! Goodbye!")
    exit()
# Initialize a variable to "True"
play_again = True
# assign the Hangman function to a variable.
game = Hangman()
# call a function within Hangman to initialize the file that contains words to guess.
game.initialize_file('words.dat')
# play the game until the user wants to quit, AND there are words to guess.
while play_again and game.num_words_available > 0:
    print("Starting game.")
    # print the number of words guessed and left to guess, and games won so far.
    game.display_statistics()
    print("\n")
    # Have game pick a word for the user to guess.
    game.new_word()
    # While user wants to continue, and the word has not been guessed,
    # ask the game to display a hangman waiting to be built, the letters available
    # and the template for the word being built. First, ask the user for a letter. If user input is not a letter,
    # or the letter has already been guessed, prompt the user again. In the hangman function, as the user guesses
    # letters, it checks to see if the letter is in the word, and if it is, it puts it in the right spot in the
    # template, if not it adds a new body part in the hangman. If the user guesses all the letters in the word OR
    # the hangman is built, the game is over. To be politically correct, this game should be called hangperson.
    while not game.game_over:
        game.display_game()
        user_guess = input("Enter a letter to guess. ")
        if not user_guess.isalpha():
            print("Sorry, I don't understand. That's not a letter. \n")
        elif not game.guess(user_guess.upper()):
            print("Sorry, you've already guessed that letter. \n")
    # Reveal the word that the computer picked.
    game.reveal_word()
    # Change the statistics to reflect the last win/loss, and print.
    game.display_statistics()
    # set the end of the game to false.
    game.game_over = False
    # Ask the user if they want to play again. If the answer is not "y", set play again to false, which ends while loop.
    # If "y", start the while loop over.
    again = input("Would you like to play again? (y/N)")
    if again.lower() != "y":
        play_again = False
# Thank the user for playing and exit.
print("Thanks for playing! Goodbye!")
exit()
