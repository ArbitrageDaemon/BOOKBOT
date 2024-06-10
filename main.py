def get_book_text(path): # open and read the book we selected
    with open(path) as f:
        return f.read()
    
def word_count(text):
    total_words = text.split() # split the text into words, total_words is an array
    return len(total_words)    # return and number of words ]

'''
#alternative to count any character, I prefered to count characters from the alphabet only
def character_count(text):
    lowered_text = text.lower()
    # Initialize an empty dictionary to store character counts
    chars = {}
    
    # Iterate through each character in the lowered text
    for char in lowered_text:
        if char in chars:
            chars[char] += 1 # if character exists add 1
        else:
            chars[char] = 1 # if character is not in dictionary give it the value
    return chars
'''

def character_count(text):
    # Initialize an empty dictionary to store character counts
    chars = {}
    lowered_text = text.lower()
    # Iterate through each character in the lowered text
    for char in lowered_text:
        # isalpha method to check if a string only contains characters from the alphabet.
        if char.isalpha():
            chars.update({char: chars.get(char,0) + 1 })
# retrieves the current count of the character, 0 as the default,           
    return chars


if __name__ == '__main__':
    book_path = "books/frankenstein.txt"
    get_book_text(book_path)
    text = get_book_text(book_path)
    total_words = word_count(text)
    char_dict = character_count(text) # dictionary that count each character
#    print(text)
#    print(total_words)
#    print(char_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")
# Sort the dictionary by value in descending order
    sorted_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
# sorting the dictionary based on the second element    
# lambda x: x[1] is a function that takes one argument x and returns the second element of x.
# Sorting a List of Tuples  dictionary.items(), the items() method returns a view object.
#  The view object contains the key-value pairs of the dictionary, as tuples in a list.
#    print(sorted_dict.items())

    for key, value in sorted_dict.items():
        print(f"The '{key}' character was found {value} times")

    
    print("--- End report ---")

'''
boot.dev solution

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
'''