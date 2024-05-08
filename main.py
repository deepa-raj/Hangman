# THIS PROBLEM IS IN REPLIT- GO THROUGH FOR EVERY STEPS

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
import random
# word_list = ["aardvark", "baboon", "camel"]


# STEP-1
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# STEP-2
#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# STEP-3
#TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#TODO-8: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
print(logo)
display = []
end_of_game = False
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
for underscore in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # this line ---> "letter = chosen_word[position]" holds the current position of the chosen word
        # this line ---> "if letter == guess:" checks the current position of the chosen word is equal to the guess word
        # if that true then assign the display position of that chosen word to the letter we guess
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])






