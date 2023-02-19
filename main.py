book_path = "books/frankenstein.txt"
def main():
        file_contents = get_book_text(book_path)
        words = get_words(file_contents)
        chars = count_letters(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        for char in sorted(chars.keys()):
             if char.isalpha() and char.islower():
                count = chars[char]
                print(f"The '{char}' character was found {count} times")

        print("--- End report ---")

def get_words(text):
    words  = text.split()
    return len(words)
    
def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_character_sums(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()



