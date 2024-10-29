import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += "_"
    return word

def spaceman(secret_word):
    letters_guessed = []
    incorrect_guess = 0
    chances = 7
    game_over = False

    print("Welcome To Spaceman")
    print("You Will Only Have 7 Tries")
    print("----------------------------------------")

    while not game_over:
        guess = input("Enter A Letter: ")
        print(letters_guessed)
        if guess in letters_guessed:
            print("You Already Guessed That Letter")
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("You have " + str(chances - incorrect_guess) + " tries")
            print("Word: " + get_guessed_word(secret_word, letters_guessed))
            print("----------------------------------------")
            if is_word_guessed(secret_word, letters_guessed):
                print("You Guessed The Word")
                game_over = True
        else:
            letters_guessed.append(guess)
            incorrect_guess += 1
            print("That Letter Is Not In The Word")
            print("You have " + str(chances - incorrect_guess) + " tries")
            print("Word: " + get_guessed_word(secret_word, letters_guessed))
            print("----------------------------------------")
            if incorrect_guess == chances:
                print("You Ran Out Of Tries, The Word Was " + secret_word)
                game_over = True
            
        if game_over:
            play_again = input("Would You Like To Play Again? (yes/no)")
            if play_again.lower() == "yes":
                load_word()
                spaceman(secret_word)
            else:
                print("Thank You For Play Spaceman")

secret_word = load_word()
spaceman(secret_word)