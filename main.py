from stats import get_book_text, count_words, count_characters, dict_to_sorted_dicts_list, dicts_list_to_string
import sys

def generate_report(path_to_book="./books/frankenstein.txt"):

    book = get_book_text(path_to_book)
    key_name = "key"
    value_name = "value"

    word_count = count_words(book)
    charactor_count_string = dicts_list_to_string(dict_to_sorted_dicts_list(count_characters(book), key_name, value_name))

    report = f""" 
============ BOOKBOT ============
Analyzing book found at {path_to_book}...
---------- Total Words ----------
{word_count}
-------- Character Count --------
{charactor_count_string}
============= END ===============
"""
    return report


def main():
    response = input("Please provide the path to the book you want analyzed. ['x' or 'X' to abort]\n")
    if response.lower() == "x":
        print("Program aborted.")
    elif response == '':
        print("Empty input detected, assuming default path.")
        print(generate_report())
    else:
        print(generate_report(response))
main()

# temp_main is just for completeing the course, I decided to go a different way with input().
def temp_main():
    if len(sys.argv) == 2:
        print(generate_report(sys.argv[1]))
    elif len(sys.argv) > 2:
        print("Too many args!")
        print("Correct Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("Missing path.")
        print("Correct Usage: python3 main.py <path_to_book>")
        sys.exit(1)
