import sys
from stats import word_count, char_count, sort_chars

def get_book_text():
    """
    Function to get the text of a book from a file.
    """
    try :
        with open(sys.argv[1], 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except OSError:
        print("Error: Unable to read the file.")
        sys.exit(1)

    
def main():
    """
    Main function to run the program.
    """
    # Get the text of the book
    book_text = get_book_text()

    # Count the number of words in the text
    words = word_count(book_text)

    # Count the number of characters in the text
    char_dict = char_count(book_text)

    # Sort the character dictionary by frequency
    sorted_chars = sort_chars(char_dict)


    print("============ BOOKBOT ============")
    print("Analyzing book found at ...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words.")

    # Print the character count
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}'")

    print("============= END ===============")

# run the main function
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

        # execute the main function
    main()