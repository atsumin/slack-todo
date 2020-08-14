import random_word
import check_word

print("Let's Hangman!")

#choose random word
random_word.random_word()

#check the guess
check_word.check_word(random_word.answer)
