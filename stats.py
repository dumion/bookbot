def get_num_words(book_text):
    count = len(book_text.split())
    return count

def get_num_chars(book_text):
    book_text = book_text.lower()
    char_dict = {}
    for char in book_text:
        if(char in char_dict):
            char_dict[char] += 1
        else: 
            char_dict[char] = 1
    return char_dict 

def sort_char_counts(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    
    def sort_on(items): 
        return items["num"]
    
    char_list.sort(key=sort_on, reverse=True)
    return char_list