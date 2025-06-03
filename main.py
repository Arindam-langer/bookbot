import stats as st

BOOKPATH = "books/frankenstein.txt"
#reads the content of the book
def get_book_text(filepath:str) ->str:
    with open(filepath) as f:
        f_content = f.read()
    return f_content ##return string
      

def main():
    book_text = get_book_text(BOOKPATH)
    num_words = st.num_of_words(book_text)
    print(f"{num_words} words found in the document")
    print(st.count_char(book_text))
if __name__ == "__main__":
    main() 