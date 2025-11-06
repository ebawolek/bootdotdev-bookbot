import sys
from stats import get_word_count, get_char_stats, get_sorted_char_stats

def get_book_text():
    try:
        with open(sys.argv[1]) as f:
            file_contents = f.read()  
        return file_contents
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



def main():
    text = get_book_text()
    count = get_word_count()
    char_stat = get_char_stats()
    char_list = get_sorted_char_stats(char_stat)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()




