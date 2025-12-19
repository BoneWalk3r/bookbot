def get_book_text(path_to_book):
    with open(path_to_book) as book:
        return book.read()
    
def count_words(text_to_be_counted):
    return f"Found {len(text_to_be_counted.split())} total words"

def main():
    print(count_words(get_book_text("./books/frankenstein.txt")))

main()