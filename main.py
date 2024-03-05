def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    num_words = get_num_words(text)
    print(f"There are {num_words} in {book_path}")
    letter_count = perform_letter_count(text)

    sorted_letter_list = []
    for letter in letter_count:
        sorted_letter_list.append({"char": letter, "num": letter_count[letter]})
    #sorted_letter_list.sort(reverse=True, key=sort_num)
    sorted_letter_list.sort(reverse=False, key=sort_char)
    
    for item in sorted_letter_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def sort_char(d):
    return d["char"]

def sort_num(d):
    return d["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def perform_letter_count(text):
    letter_count = {}
    lowered_text = text.lower()

    for i in range(0, len(text)):
        #print(f"--Checking for {lowered_text[i]}...")
        if lowered_text[i] in letter_count:
            letter_count[lowered_text[i]] += 1
            #print(f"Found it! new count for {lowered_text[i]} is {letter_count[lowered_text[i]]}")
        else:
            letter_count[lowered_text[i]] = 1
            #print(f"New letter {lowered_text[i]} added to dictionary, count is {letter_count[lowered_text[i]]}")

    return letter_count

main()