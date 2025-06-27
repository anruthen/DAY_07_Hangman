import random
import hangman_art
import hangman_words

lives = 6
chosen_word = random.choice(hangman_words.word_list)
print("Welcome to")
print(hangman_art.logo)
display = ["_"] * len(chosen_word)
word_length = len(chosen_word)

while "_" in display and lives > 0:
    guess = input("Guess a letter: \n").lower()
    if guess in display:
        print(f"You already guessed the letter '{guess}'")
    if guess in chosen_word:
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess 
        print(hangman_art.stages[lives])
        print(''.join(display))
    else:
        lives -= 1
        print(hangman_art.stages[lives])
        print(''.join(display))
        print(f"The letter {guess} was not in the word.")
        print(f"You have {lives}/6 lives left.")

if lives == 0:
    print(f"The word was {chosen_word}. You lose.")
elif "_" not in display:
    print(f"Congratulations. You win.")
