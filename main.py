from stats import count_words
from stats import count_character
from stats import sort_character
import sys


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()



def main():
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

    book_path = sys.argv[1]

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    print("---------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("------- Character Count -------")
    characters = count_character(text)
    sorted_chars = sort_character(characters)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ==============")



if __name__ == "__main__":
  main()
