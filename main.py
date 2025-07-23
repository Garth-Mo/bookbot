from stats import get_num_words, character_count, sort_on, dict_sort
import sys

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def main():
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    num_characters = character_count(text)
    sorted_characters = dict_sort(num_characters)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {sys.argv[1]}")
    print("\n------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("\n------------ Character Count ------------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============ END ============")

def get_book_text(path):
    with open(path) as f:
        return f.read()




main()