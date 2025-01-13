def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(word_count(file_contents))
    #print(char_count(file_contents))
    print_report("books/frankenstein.txt", word_count(file_contents), char_count(file_contents))

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
    sorted_char_count = 
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for ch in char_count:
        print(f"The '{ch}' character was found {char_count[ch]} times")
    print("--- End report ---")

main()