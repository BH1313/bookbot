from stats import count_words
from stats import count_character
from stats import sort_character

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  text = get_book_text("./books/frankenstein.txt")

  num_words = count_words(text)
  #print(f"Found {num_words} total words")

  characters = count_character(text)
  sorted_characters = sort_character(characters)

######CLI#UI############
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"(Found {num_words} total words")
  print("--------- Character Count -------")
  print(sorted_characters)
  print("============= END ===============")

if __name__ == "__main__":
  main()
