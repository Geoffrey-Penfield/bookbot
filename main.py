def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict_list = convert_dict_to_sorted_dict_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words in book.")
    print()

    for item in sorted_dict_list:
        if item["letter"].isalpha():
            print(f"The '{item["letter"]}' character appears {item["count"]} times.")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def convert_dict_to_sorted_dict_list(dict):
    sorted_list = []
    for item in dict:
        sorted_list.append({"letter" : item, "count" : dict[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["count"]

main()