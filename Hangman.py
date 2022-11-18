from HangmanStages import getHangmanStages
from Words import word_list
import random
import os

clear = lambda: os.system('clear')

def GetRandomWordFromWordList():
  return random.choice(word_list).upper()
  
def FillLettersInWord(word, guess):
  global secret_word
  real_word = word
  for i, letter in enumerate(real_word):
    if letter != "_" and guess == letter:
      secret_word[i] = letter
  
def setUpVariables():
  global count
  global already_guessed
  global lenght
  global guessed
  global tries
  global secret_word
  count = 0
  already_guessed = []
  guessed = False
  tries = 8
  


def play(word):
  global count
  global display
  global already_guessed
  global secret_word
  lenght = len(word)
  secret_word = ["_"] * lenght
  tries = 8
  msg = ""
  word_to_guess = word
  
  while not guessed and tries > 0:
    clear()
    print(getHangmanStages(tries))
    print(msg)
    guess = input("Word to guess: " + "".join(secret_word) + " \nEnter your guess: ").upper()
    guess.strip()
    if not guess.isalpha():
      msg = "Es sind nur Buchstaben erlaubt!"
    
    if guess in already_guessed:
      msg = "Verwendete Buchstaben: '" + guess + "'"
    
    if guess in word and guess.isalpha():
      clear()
      print(getHangmanStages(tries))
      already_guessed.extend([guess])
      FillLettersInWord(word, guess)
      msg = "Das gesuchte Wort enthält den Buchstaben '" + guess + "'"
    else:
      if guess.isalpha():
        clear()
        tries -= 1
        print(getHangmanStages(tries))
        msg = "Das gesuchte Wort enthält den Buchstaben '" + guess + "' nicht"
      else:
        msg = "Es sind nur Buchstaben erlaubt!"
        
    
        
    if '_' not in secret_word or guess == word:
      clear()
      print("Du hast gewonnen")
      print("übrige versuche: " + str(tries))
      break
    
  if tries == 0:
    msg = "Das gesuchte Wort war: " + word
    print(msg)
    print("Leider verloren, vielleicht ja nächstes mal")
    
setUpVariables()
play(GetRandomWordFromWordList())