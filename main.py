from stats import get_num_words
from stats import get_num_character

def main():
      book_path = "books/frankenstein.txt"
      book_text = get_book_text(book_path)

      number_words = get_num_words(book_text)
      print(f"{number_words} words found in the document")

      number_characters = get_num_character(book_text)
      print(number_characters)

def get_book_text(book_path):
        with open(book_path) as f:
            return f.read()



main()