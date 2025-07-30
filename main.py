from stats import count_words, count_chars, sort_chars
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_boot_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_boot_text(sys.argv[1])
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_chars(char_count)

    # Report printing

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for c in sorted_chars:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")

    print("============ END ===============")

main()