import random
import pytest

#Brycyn Barreras
#CIS 256 Spring 2026
# Exercise Assignment 4


fruit_list = ["orange", "apple", "banana", "grape"]     #input the lists to test for all lists

animal_list = ["dog", "cat", "pig", "duck"]

color_list = ["blue", "green", "orange", "purple" ]

all_list = fruit_list + animal_list + color_list        #store all the lists into one


def test_word_checking():           #test to check for if word is found in the lists

    word = random.choice(all_list)      #select a random word from all the list

    assert word in all_list     #test if it is true that word is in the lists

def test_incorrect_guess():     #test for an incorrect guess

    word = "dog"        #set the word

    guess = "p"         #take the guess input

    guess_attempts = 5      #take the number of guess attempts

    if guess not in word:       #if the guess is not in the word

        guess_attempts -= 1     #then a guess attempt is taken away


    assert guess not in word        #verify that it is true that the guess is not in the word

    assert guess_attempts == 4      #make sure that guess_attempts are properly being taken away for wrong guesses


def test_correct_guess():   #test for correct guess

    word = "blue"       #set word

    guess = "u"         #set guess

    correct_guess = guess in word       #set the value for a correct guess which would be that the guess is in the word

    assert correct_guess is True        #verify that correct_guess is a true statement

    assert guess == "u"     #ensure the proper value for the guess


def test_guessing_word():       #test for guessing the whole word


    word = "grape"

    guess = "grape"


    assert guess == word        #test that it is true that the guess and word match values


def test_guessing_word_wrong():     #test for guessing the wrong word


    word = "grape"

    guess = "apple"

    guess_attempts = 5

    guess_attempts -= 1

    assert guess != word        #test that guess is not equal to the word

    assert guess_attempts == 4  #test that guest_attempts are properly being subtracted for wrong guesses