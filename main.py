def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    list_of_chars = convert_dict_to_array(chars_dict)
    list_of_chars.sort(reverse=True, key=sort_on)
    print(list_of_chars)

def sort_on(dict):
    return dict["count"]

def convert_dict_to_array(dict):
    array = []
    for entry in dict:
        if entry.isalpha():
            array.append({"name": entry, "count": dict[entry]})
    return array

def get_char_count(text):
    dictionary_of_characters = {}
    for c in text.lower():
        if c in dictionary_of_characters:
            dictionary_of_characters[c] += 1
        else:
            dictionary_of_characters[c] = 1 
    return dictionary_of_characters

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
