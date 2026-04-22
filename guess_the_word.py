import random

#Brycyn Barreras
#CIS256 Spring 2026
#Exercise Assignment 4

fruit_list = ["orange", "apple", "banana", "grape"]

animal_list = ["dog", "cat", "pig", "duck"]

color_list = ["blue", "green", "orange", "purple" ]


user_choice = input("Choose Category (Fruits, Animals, Colors): ").lower()

if user_choice == "fruits":

    word = random.choice(fruit_list).lower()

    guess_attempts = 7
    letter_guesses = set()

    print("Success: Your word is a random fruit")

elif user_choice == "animals":

    word = random.choice(animal_list).lower()

    guess_attempts = 5
    letter_guesses = set()


    print("Success: Your word is a random animal")

elif user_choice == "colors":

    word = random.choice(color_list).lower()

    guess_attempts = 7
    letter_guesses = set()


    print("Success: Your word is a random color")

else:

    random_choice = random.randint(1, 3)

    if random_choice == 1:

        word = random.choice(fruit_list).lower()

        guess_attempts = 7
        letter_guesses = set()
        
        category = "fruits"

        print(f"Invalid Input: Your Category is {category}")

    elif random_choice == 2:

        word = random.choice(animal_list).lower()
        
        guess_attempts = 5
        letter_guesses = set()

        category = "animals"

        print(f"Invalid Input: Your Category is {category}")

    elif random_choice == 3:

        word = random.choice(color_list).lower()

        guess_attempts = 7
        letter_guesses = set()

        category = "colors"

        print(f"Invalid Input: Your Category is {category}")



print("\n---Word Guessing---\n")
print(f"You have {guess_attempts} attempts and the word is {len(word)} letters")

while guess_attempts > 0:

    guesses_displayed = ""

    for letter in word:

        if letter in letter_guesses:

            guesses_displayed += letter + " "

        else:

            guesses_displayed += "_ "


    print(f"\nYour Word: {guesses_displayed.strip()}")

    print(f"Current Guesses: {sorted(letter_guesses)}")

    print(f"Remaining Attempts: {guess_attempts}")

    if "_" not in guesses_displayed:

        print("\nAll Letters Found!")
        print("Congratulations!")
        break


    guess = input("\nEnter your guess: ").lower()

    if len(guess) > 1:

        if guess == word:

            print("Whole Word Found!")

            for let in word:

                letter_guesses.add(let)
                

        else:

            print("Incorrect Guess")

            guess_attempts -= 1

    elif len(guess) == 1:

        if guess in letter_guesses:

            print("Letter already guessed")
            continue

        letter_guesses.add(guess)

        if guess in word:

            print("Letter Found")


        else: 

            print("Letter not found")

            guess_attempts -= 1


if guess_attempts == 0:

    print("\n------Game Over------")
    print("No Guess Attempts Left\n")
    print(f"Your word was {word}")


    