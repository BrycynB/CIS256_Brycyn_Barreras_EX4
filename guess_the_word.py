import random

#Brycyn Barreras
#CIS256 Spring 2026
#Exercise Assignment 4

fruit_list = ["orange", "apple", "banana", "grape"]     #create different list options for user to choose type of random words

animal_list = ["dog", "cat", "pig", "duck"]

color_list = ["blue", "green", "orange", "purple" ]


user_choice = input("Choose Category (Fruits, Animals, Colors): ").lower()      #prompt user to select choice, disregarding case sensitivity

if user_choice == "fruits":                 #create if-else statements for what user chooses

    word = random.choice(fruit_list).lower()        #select a random word from the fruit list, disregarding case sensitivity

    guess_attempts = 7          #set a number of guess attempts the user has for this list
    letter_guesses = set()      #create a set to store the guesses that the user has made

    print("Success: Your word is a random fruit")

elif user_choice == "animals":      #elif statement for animal list

    word = random.choice(animal_list).lower()

    guess_attempts = 5      #5 guesses for animal list
    letter_guesses = set()


    print("Success: Your word is a random animal")

elif user_choice == "colors":       #statement for color list

    word = random.choice(color_list).lower()

    guess_attempts = 7
    letter_guesses = set()


    print("Success: Your word is a random color")

else:       #else statement that handles if the user enters anything except one of the given options

    random_choice = random.randint(1, 3)        #store a random number 1-3 for the options

    if random_choice == 1:      #if the random number is 1 then the user will get fruit list

        word = random.choice(fruit_list).lower()

        guess_attempts = 7
        letter_guesses = set()
        
        category = "fruits"     

        print(f"Invalid Input: Your Category is {category}")    #output message letting the user know they got fruit list

    elif random_choice == 2:        #random number 2 will select animal list

        word = random.choice(animal_list).lower()
        
        guess_attempts = 5
        letter_guesses = set()

        category = "animals"

        print(f"Invalid Input: Your Category is {category}")

    elif random_choice == 3:        #random number 3 will select color list 

        word = random.choice(color_list).lower()

        guess_attempts = 7
        letter_guesses = set()

        category = "colors"

        print(f"Invalid Input: Your Category is {category}")



print("\n---Word Guessing---\n")
print(f"You have {guess_attempts} attempts and the word is {len(word)} letters")        #output message with guess attempts based on the list they received  
                                                                                        #and how long their word is

while guess_attempts > 0:       #while loop to run while there are still guess attempts 

    guesses_displayed = ""      #string to display the guesses that are made

    for letter in word:         #iterate through each letter in the selected word

        if letter in letter_guesses:        #if the letter in the current iteration matches the letter give in the letter_guesses set, add the letter to guesses_displayed

            guesses_displayed += letter + " "       #adds the letter and a " " for readability

        else:

            guesses_displayed += "_ "       #if letter does not match then a "_" and " " are added for readability


    print(f"\nYour Word: {guesses_displayed.strip()}")      #print the users word without any trailing or leading blank spaces

    print(f"Current Guesses: {sorted(letter_guesses)}")     #print the users guesses

    print(f"Remaining Attempts: {guess_attempts}")          #print number of attempts remaining

    if "_" not in guesses_displayed:        #if there are no longer any blank spaces in the guesses_displayed string, break out the loop and user wins 

        print("\nAll Letters Found!")
        print("Congratulations!")
        break


    guess = input("\nEnter your guess: ").lower()   #get the user guess and ignore case sensitivity

    if len(guess) > 1:      #test if the length of the guess is longer than 1 character to test if they are guessing the whole word

        if guess == word:       #if they guess the whole word correctly, output message

            print("Whole Word Found!")

            for let in word:        #add each letter of the word to the guesses

                letter_guesses.add(let)
                

        else:               #if incorrect guess of the whole word, output message and take away a guess attempt

            print("Incorrect Guess")

            guess_attempts -= 1

    elif len(guess) == 1:       #if user is only guessing 1 letter

        if guess in letter_guesses:             #test if the guess is already in the letter_guesses

            print("Letter already guessed")
            continue        #continue back to the top of the loop

        letter_guesses.add(guess)       #add the guess to the letter_guesses if it is not already guessed (this works because we get past the continue)

        if guess in word:           #output message if letter is found in the word

            print("Letter Found")


        else:       #if letter is not found then output message and remove a guess

            print("Letter not found")

            guess_attempts -= 1


if guess_attempts == 0:     #if guess_attempts hit 0 then output message and reveal the word

    print("\n------Game Over------")
    print("No Guess Attempts Left\n")
    print(f"Your word was {word}")


    