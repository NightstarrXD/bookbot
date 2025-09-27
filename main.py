def get_book_text(file):
    contents = None
    with open(file) as f:
        contents = f.read()
    return contents
from stats import count_words
from stats import count_characters
def main():
    count_words(get_book_text("books/frankenstein.txt"))
    count_characters(get_book_text("books/frankenstein.txt"))
main()