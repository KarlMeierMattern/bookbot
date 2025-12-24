def count_words(book_text):
    return (len(book_text.split()))

def char_count(book_text):
    char_dict = {}
    for char in list(book_text.lower()):
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(item):
    return item[1]

def sort_char_dict(char_dict):
    items = list(char_dict.items())
    items.sort(key=sort_on, reverse=True)
    return items