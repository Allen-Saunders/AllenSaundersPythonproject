import random 
import sys
from termcolor import colored

# code shows the used imports for the project aswell as it uses the "words.txt" file to draw words for the list.

def print_menu():
  print("Allen Saunders Wordle Project")
  print("Type A 5 Letter Word, Press Enter When Fully Typed.\n")

def read_random_word():
  with open("words.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)

print_menu()

play_again = ""
while play_again != "q":
  word = read_random_word()
  print(word)

    # code shows the random choosing of the word with the use of the "import random" and the use of the "words.txt" file. code also prompts the user to type a word.
  
  for guess in range(1, 7):
      attempt = input().lower()
    
      # code allows for the ammount of guesses to be 5.
    
      sys.stdout.write('\x1b[1A')
      sys.stdout.write('\x1b[2K')
    
      for guess in range( min(len(attempt), 5) ):
          if attempt[guess] == word[guess]:
            print(colored(attempt[guess], 'green'), end="")
          elif attempt[guess] in word:
            print(colored(attempt[guess], 'yellow'), end="")
          else:
            print(attempt[guess], end="")
      print()

    # code shows the limited ammount of characters used along with the system that shows the use of the letter in the word and if its in the proper column.
    
      if guess == word:
        print(colored(f"Congrats! You got the wordle in {guess}", 'red'))
        break
      elif attempt == 6:
            print(f"Sorry the wordle was {word}")
play_again = input("Want to play again? Type q to QUIT")
# section of code shows display messages for either winning or losing the game. *EDIT* CODE NON-FUNCTIONAL FOR UNKNOWN REASON - TAKE UP WITH MR.KAUNE ON EXAM DAY