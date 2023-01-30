import random 
import sys
from termcolor import colored

# code shows the used imports for the project aswell as it uses the "words.txt" file to draw words for the list

def print_menu():
  print("Allen Saunders Wordle Project")
  print("Type A 5 Letter Word, Press Enter When Fully Typed.")

def read_random_word():
  with open("words.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)

print_menu()
word = read_random_word()

# code shows the random choosing of the word with the use of the "import random" and the use of the "words.txt" file. code also prompts the user to type a word

for guess in range(1, 7):
  attempt = input().lower()

  for i in range( min(len(attempt), 5) ):
      if attempt[i] == word[i]:
        print(colored(attempt[i], 'green'), end="")
      elif attempt[i] in word:
        print(colored(attempt[i], 'yellow'), end="")
      else:
        print(attempt[i], end="")

  if attempt  == word:
    print(colored(f"congrats you've been worded. you got the answer in {guess}", 'red'))
    break 