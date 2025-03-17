def get_book_text(file):
    with open(file) as f:
        contents = f.read()
        return contents

def get_count_words(file) -> int:
    with open(file) as f:
        text = f.read()
        words = text.split()
        
        return len(words)

def count_characters(file):
    with open(file) as f:
        text = f.read()
        
    characters = {}
        
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
        
    return characters

def sort_on(dictionary):
    return dictionary["num"]

def chars_to_sorted_list(num_chars):
    sorted_list = []
    for char in num_chars:
        sorted_list.append({"char": char, "num": num_chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list