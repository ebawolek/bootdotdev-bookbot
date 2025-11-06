import sys
def get_word_count():
    with open(sys.argv[1]) as f:
        words = f.read().split()
        word_count = len(words)
    return f"Found {word_count} total words"

def get_char_stats():
    with open(sys.argv[1]) as f:
        lower_char = f.read().lower()
        counts = {}
        for c in lower_char:
            counts[c] = counts.get(c, 0) + 1
        return counts

def sort_on(counts):
    return counts["num"]

def get_sorted_char_stats(counts):
    #Convert dictionary to list of dictionaries
    char_list = []
    for char, count in counts.items():
        if char.isalpha(): #Only include alphabetical characters
            char_list.append({"char": char, "num": count})
    
    # Sort from greatest to least using the helper function
    char_list.sort(reverse=True, key=sort_on)
    return char_list



