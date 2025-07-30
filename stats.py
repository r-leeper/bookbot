def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_chars(char_count):
    list_of_chars = []
    for i in char_count:
        list_of_chars.append({"char": i, "num": char_count[i]})
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars


# Test code
if __name__ == "__main__":
    # Create a sample dictionary to test sorted_chars
    test_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
    print("Testing sorted_chars function:")
    print("Input dictionary:", test_dict)
    result = sort_chars(test_dict)
    print("Result:", result)
