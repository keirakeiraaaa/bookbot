def get_word_count(book_text):
      # convert book_text into a string
      text_string = str(book_text)

      # then convert that string into a list
      text_list = text_string.split()

      # then have computer count number of items inside list :)
      return len(text_list)