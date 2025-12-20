from stats import get_book_text, count_words, count_characters

def main():
    print(count_words(get_book_text("./books/frankenstein.txt")))
    print(count_characters(get_book_text("./books/frankenstein.txt")))

main()