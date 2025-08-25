from stats import get_num_words
from stats import get_num_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return  f.read()



def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    # print(text)
    print(f"{num_words} words found in the document")
    print(get_num_characters(text))
    
main()