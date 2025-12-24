import sys
from stats import count_words, char_count, sort_char_dict

def get_book_test(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_test(file_path)
    word_count =count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")    
    char_dict = char_count(book_text)
    sorted_char_dict = sort_char_dict(char_dict)
    for char, count in sorted_char_dict:
        print(f"{char}: {count}")
    print("============= END ===============")


main()