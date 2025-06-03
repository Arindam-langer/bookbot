def num_of_words(text: str) -> int:
    num_words = len(text.split())
    return num_words 


def count_char(text :str) -> dict:
    text = text.lower()
    char_cnt = dict()
    for i in text:
        if i in char_cnt:
            char_cnt[i] +=1
        else:
            char_cnt[i] = 1
    return char_cnt 