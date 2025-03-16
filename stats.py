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