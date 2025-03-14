def get_book_text(file):
    with open(file) as f:
        contents = f.read()
        return contents
    
def Count_words(file) -> int:
    with open(file) as f:
        text = f.read()
        words = text.split()
        
        return len(words)

def main():
    
    file_path = "books/frankenstein.txt"
    book = get_book_text(file_path)
    num_words = Count_words(file_path)
    print(book)
    print(f"\n{num_words} words found in the document")

main()