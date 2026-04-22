import random
import pytest

#Brycyn Barreras
#CIS 256 Spring 2026
# Exercise Assignment 4


fruit_list = ["orange", "apple", "banana", "grape"]

animal_list = ["dog", "cat", "pig", "duck"]

color_list = ["blue", "green", "orange", "purple" ]

all_list = fruit_list + animal_list + color_list


def test_word_checking(): 

    word = random.choice(all_list)

    assert word in all_list

def test_incorrect_guess():

    word = "dog"

    guess = "p"

    guess_attempts = 5

    if guess not in word:

        guess_attempts -= 1


    assert guess not in word

    assert guess_attempts == 4


def test_correct_guess():

    word = "blue"

    guess = "u"

    correct_guess = guess in word

    assert correct_guess is True

    assert guess == "u"


def test_guessing_word():


    word = "grape"

    guess = "grape"


    assert guess == word


def test_guessing_word_wrong():


    word = "grape"

    guess = "apple"

    guess_attempts = 5

    guess_attempts -= 1

    assert guess != word

    assert guess_attempts == 4