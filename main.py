def get_book_text(path_to_book):
    with open(path_to_book) as book:
        text = book.read()
    return text
    
def main():
    print(get_book_text("./books/frankenstein.txt"))

main()