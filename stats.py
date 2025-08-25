def get_num_words(text):
    # number = text.split()
    return len(text.split())

def get_num_characters(text):
    characters = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters