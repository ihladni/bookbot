
def counter(s):
    words = s.split()
    return len(words)

# Moje rješenje
def count_each_char(s):
    lower_string = s.lower()
    slova = {}
    for char in lower_string:
        if char in slova:
            slova[char] = slova[char] + 1
        else:
            slova[char] = 1
    
    return slova
    
    """
    for key_slovo in slova:
        print(f"{key_slovo}: {slova[key_slovo]}")
    """

def sort_on(d):
    return d["num"]

# da bi se sortirali, ovo sam kopirao, nisam vidio jos ovakvo debiliranje
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def dict_report_printer(s, fname):
    broj_rijeci = counter(s)
    dict = count_each_char(s)
    sortedList = chars_dict_to_sorted_list(dict)
    

    print(f"--- Begin report of {fname} ---")   
    print(f"{broj_rijeci} words found in the document")
    print("")

    """
    dict2 = {}
    for si in sortedList:
        dict2[si["char"]] = si["num"]

    for key_slovo in dict2:
        if key_slovo.isalpha():
            print(f"The '{key_slovo}' character was found {dict[key_slovo]} times")
    """

    for si in sortedList:
        if si["char"].isalpha():
            print(f"The '{si["char"]}' character was found {si["num"]} times")

    print("--- End report ---")


# Njihovo rješenje
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def main():
    file_contents = ""
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    # print(file_contents)
    # slova_dict = count_each_char(file_contents)
    # print (slova_dict)
    dict_report_printer(file_contents, path_to_file)

main()