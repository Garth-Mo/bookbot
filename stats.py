def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_case = text.lower()
    characters_dict = {}
    for character in lower_case:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict

def sort_on(items):
    return items["num"]

def dict_sort(dictionary):
    result = []
    for key, value in dictionary.items():
        if key.isalpha():
            result.append({"char": key, "num": value})
    result.sort(reverse=True, key=sort_on)
    return result

