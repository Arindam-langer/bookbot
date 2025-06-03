import stats as st
import sys

args = sys.argv
BOOKPATH = str(args[0])
#reads the content of the book
def get_book_text(filepath:str) ->str:
    with open(filepath) as f:
        f_content = f.read()
    return f_content ##return string

#pretty print
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")      

def main():
    book_text = get_book_text(BOOKPATH)
    num_words = st.num_of_words(book_text)
    chars_dict = st.count_char(book_text)
    chars_sorted_list = st.chars_dict_to_sorted_list(chars_dict)
    print_report(BOOKPATH, num_words, chars_sorted_list)
if __name__ == "__main__":
    main() 