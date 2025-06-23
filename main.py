from stats import get_word_count

def main():
      book_path = "books/frankenstein.txt"
      book_text = get_book_text(book_path)

      number_words = get_word_count(book_text)
      print(f"{number_words} words found in the document")

def get_book_text(book_path):
        with open(book_path) as f:
            return f.read()



main()