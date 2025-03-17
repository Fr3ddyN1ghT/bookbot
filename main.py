import sys

from stats import (
    get_count_words,
    get_book_text,
    count_characters,
    chars_to_sorted_list
)

    

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    num_words = get_count_words(file_path)
    counted_chars = count_characters(file_path)
    chars_sorted_list = chars_to_sorted_list(counted_chars)
    print_report(file_path, num_words, chars_sorted_list)
    

def print_report(file_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()