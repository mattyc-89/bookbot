def word_count(text):
    """
    Function to count the number of words in a text.
    """
    # Split the text into words
    words = text.split()
    
    # Count the number of words
    num_words = len(words)
    
    return num_words

def char_count(main):
    """
    Function to count the number of characters in a text.
    """
    # Convert the text to lowercase
    lower_case = main.lower()

    # Count the number of characters
    num_chars = len(lower_case)

    char_dict = {}

    for char in lower_case:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(dict_item):
    """
    Helper function to return the count value from a dictionary.
    Used as the key for sorting.
    """
    return dict_item["count"]

def sort_chars(char_dict):
    """
    Function to sort the character dictionary by frequency.
    Returns a sorted list of dictionaries.
    """
    # Create a list of dictionaries
    chars_list = []
    
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list by count in descending order
    chars_list.sort(key=sort_on, reverse=True)
    
    return chars_list