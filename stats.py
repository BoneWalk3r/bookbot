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

def dict_to_sorted_dicts_list(dict, key_name, value_name):
    """
    Takes a dictionary and turns each key/value pair into it's own dictionary, which is then put in a list.\n
    'key_name' is the label assigned to the key of a given pair, while 'value_name' does the same for the given value of that same pair.
    """
    result = []
    intermediary_dict = {}
    get_value = lambda x: x[f"{value_name}"]
    for entry in dict:
        intermediary_dict[f"{key_name}"] = entry
        intermediary_dict[f"{value_name}"] = dict[entry]
        result.append(intermediary_dict)
        intermediary_dict = {}
    
    result.sort(reverse=True, key=get_value)

    return result

def dicts_list_to_string(list_of_dicts):
    result = ""
    expect_number = False
    for dict in list_of_dicts:
        for key in dict:
            if f"{dict[key]}".isalpha():
                result += f"{dict[key]}: "
                expect_number = True
            elif expect_number:
                result += f"{dict[key]}\n"
                expect_number = False
            else:
                pass
    
    result = result.rstrip()
    return result


#print(dicts_list_to_string(dict_to_sorted_dicts_list(count_characters(get_book_text("./books/frankenstein.txt")), "char", "num")))