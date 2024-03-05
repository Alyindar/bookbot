import sys

def main():
    if len(sys.argv) == 1:
        print("##Error##: a path to a text file is required to process.")
        print("For a description of the usage, use command: main.py -help")
        exit()

    if sys.argv[1] == "h" or sys.argv[1] == "-h" or sys.argv[1] == "-help" or sys.argv[1] == "help":
        print("bookbot: Prints the word and letter count for the contents of a booko")
        print("Usage:")
        print("  main.py book [sort_order]")
        print("  book: The path of the book you wish to parse.")
        print("  sort_order: Optional; Sort the letter list by -c count or -l letter. Default is sort by count.")
        print("Example: main.py books/frankenstein.txt -c")
        exit()

    book_path = sys.argv[1]
    if len(sys.argv) > 2:
        sort_order = sys.argv[2].lower()
        if sort_order != "-c" and sort_order != "-l":
            print("##ERROR##: an invalid sort order was specified")
            print("For a description of the usage, use command: main.py -help")
            exit()
    else:
        sort_order = "-c"

    try:
        text = get_book_text(book_path)
    except Exception as e:
        print(e)
        print("##ERROR##: An invalid book path was specified!")
        print("For a description of the usage, use command: main.py -help")
        exit()
    num_words = get_num_words(text)
    print(f"There are {num_words} words in {book_path}")
    letter_count = perform_letter_count(text)

    sorted_letter_list = []
    for letter in letter_count:
        sorted_letter_list.append({"char": letter, "num": letter_count[letter]})
    if sort_order == "-c":
        sorted_letter_list.sort(reverse=True, key=sort_num)
    elif sort_order == "-l":
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
        if lowered_text[i] in letter_count:
            letter_count[lowered_text[i]] += 1
        else:
            letter_count[lowered_text[i]] = 1

    return letter_count

main()