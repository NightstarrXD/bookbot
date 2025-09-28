def get_book_text(file):
    contents = None
    with open(file) as f:
        contents = f.read()
    return contents
from stats import count_words
from stats import count_characters
from stats import sort_by_greatest
def main():
    book_analized = get_book_text("books/frankenstein.txt")
    print(
        "==================== BookBot ===================="
    )
    print(
        "Analyzing book found at books/frankenstein.txt..."
    )
    print(
        "------------------ Word Count -------------------"
    )
    count_words(book_analized)
    print(
        "---------------- Character Count ----------------"
    )
    characters_counted = count_characters(book_analized)
    sorted_list = sort_by_greatest(characters_counted)
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["count"]}")
    print(
        "====================== End ======================"
    )
main()