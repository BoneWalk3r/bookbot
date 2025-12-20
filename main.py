from stats import count_words, get_book_text

def main():
    print(count_words(get_book_text("./books/frankenstein.txt")))

main()