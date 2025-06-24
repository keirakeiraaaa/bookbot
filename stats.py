def get_num_words(book_text):
      # then convert that string into a list
      text_list = book_text.split()

      # then have computer count number of items inside list :)
      return len(text_list)

def get_num_character(book_text):
    book_text = book_text.lower()
    count_num = {}
    for letter in book_text:
        if letter in count_num:
            count_num[letter] += 1
        else:
            count_num[letter] = 1
    return count_num

def sort_on(count):
    return count["num"]

def get_sort_data(number_char):
    sorted_list = []
    for letter in number_char:
        if letter.isalpha() == True:
            combined_dict = {"char" : letter, "num" : number_char[letter]}
            sorted_list.append(combined_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
