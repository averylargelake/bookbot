from curses.ascii import isalpha


def main():
    b_path = "books/frankenstein.txt"
    text = read_file(b_path)
    count = get_words(text)
    char_count = count_words(text)
    list = process_into_list(char_count)
    wall_of_text(list, count)
    
def read_file(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    return len(text.split())

def count_words(words):
    count = {}
    for word in words:
        w = word.lower()
        if w not in count:
            count[w] = 1
        else:
            count[w] += 1
    return count

def process_into_list(char_count):
    list = []
    for c in char_count:
        if  isalpha(c):
            list.append({f"char": c, "key": char_count[c]})
    return list

def sort_on(dict):
    return dict["key"]

def wall_of_text(list, count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    reverse = sorted(list, reverse=True, key=sort_on)
    print(list)
    print(reverse)
    for r in reverse:
        print(f"The {r['char']} character was found {r['key']} times")
    print("--- END Report ---")

main()