#Step 5

import random
import hangman_words
import hangman_art


#use random library to generate random word from word list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# A conditional statement used throughout the game.
end_of_game = False

# set lives = to 6 to represent each life on hangman.
lives = 6

# Prints the hangman logo imported from hangman_art.py
print(hangman_art.logo)

#Testing code. Comment out if necessary
print(f'Pssst, the solution is {chosen_word}.')

# An array that will print underlines for each letter in the random word
display = []
for _ in range(word_length):
    display += "_"

# While loop and its contents will continue to run until end_of_game is True.
while not end_of_game:
    # User enters a letter which is stored in the variable guess. Lowered.
    guess = input("Guess a letter: ").lower()

    # If the user has already entered a correct guess, they will be notified.
    if guess in display:
        print(f"You have already gussed the letter {guess} correctly. Please use a different letter.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Your guess {guess} is incorrect. You now lose a life. Please try a different letter.")
        lives -= 1
        # If user runs out of lives, the game will end and end_of_game will be set to True.
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py to display each stage of the hangman game.
    print(hangman_art.stages[lives])