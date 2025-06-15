import random

word_list = ["aardvark", "baboon", "camel"]
blanks = ""

# Randomly choose a word
chosen_word = random.choice(word_list)
print(chosen_word)

# let user guess a word
game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose.")

    print(lives)

    if "_" not in display:
        game_over = True
        print("You win.")
