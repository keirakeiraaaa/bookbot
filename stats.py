def get_num_words(book_text):
      # then convert that string into a list
      text_list = book_text.split()

      # then have computer count number of items inside list :)
      return len(text_list)

def get_num_character(book_text):
    count_num = {}


    for letters in book_text:
         if letters in count_num:
              count_num[letters] += 1
    return count_num