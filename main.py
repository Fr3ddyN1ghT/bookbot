from stats import get_count_words
from stats import count_characters

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
        return contents
    

def main():
    
    file_path = "books/frankenstein.txt"
    book = get_book_text(file_path)
    num_words = get_count_words(file_path)
    print(book)
    print(f"\n{num_words} words found in the document")
    
    counted_chars = count_characters(file_path)
    print(f"\n{counted_chars}")

main()