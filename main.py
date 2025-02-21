import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    #print(word_count(file_contents))
    #print(char_count(file_contents))
    file = sys.argv[1]
    print_report(file, word_count(file_contents), char_count(file_contents))

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_set = set(["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    target_text = text.lower()
    result = {}
    for ch in target_text:
        if ch in char_set:
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1
    return result

def print_report(file_name, word_count, char_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for ch in char_count:
        print(f"{ch}: {char_count[ch]} times")
    print("--- End report ---")

main()