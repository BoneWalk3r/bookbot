def get_book_text(path_to_book):
    with open(path_to_book) as book:
        return book.read()
    
def count_words(text_to_be_counted):
    return f"Found {len(text_to_be_counted.split())} total words"

def count_characters(text_to_be_counted):
    simplified_text = text_to_be_counted.lower()
    results = {}
    for character in simplified_text:
        if character in results:
            results[character] = results[character] + 1
        else:
            results[character] = 1
    return results