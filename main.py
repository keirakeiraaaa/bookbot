import sys
from stats import get_num_words
from stats import get_num_character
from stats import get_sort_data

def main():
      # book_path = "books/frankenstein.txt"
      if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

      book_path = sys.argv[1]
      book_text = get_book_text(book_path)

      number_words = get_num_words(book_text)

      number_characters = get_num_character(book_text)
      # print(number_characters)

      sort_data = get_sort_data(number_characters)


      # pretty printing to make the output look nice
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {book_path}...")
      print("----------- Word Count ----------")
      print(f"Found {number_words} total words")
      print("--------- Character Count -------")

      for item in sort_data:
            print(f"{item['char']}: {item['num']}")
      
      print("============= END ===============")
      
      

def get_book_text(book_path):
        with open(book_path) as f:
            return f.read()


main()