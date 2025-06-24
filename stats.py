def get_num_words(book_text):
      # then convert that string into a list
      text_list = book_text.split()

      # then have computer count number of items inside list :)
      return len(text_list)

def get_num_character(book_text):
    count_num = {
         "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0
    }

    for letters in book_text:
         if letters in count_num:
              count_num[letters] += 1
    return count_num