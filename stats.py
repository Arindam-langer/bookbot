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

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list