def print_menu():
  print("AllenSaundersWordleProject")
  print("Type A 5 Letter Word, Press Enter When Fully Typed.")

def read_random_word():
  with open("words.txt") as f:
    words = f.read().splitlines()

print_menu()