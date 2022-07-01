import re


def table_creator(table_list):
    print("FRUIT AMOUNT PRICE")
    for fruit, quantity, price in table_list:
        print(
            f"{fruit:7s}{quantity: ^5d} "
            f"${price: <8.2f}")


def splitter(sentence):
    sentence = sentence.title()
    words = sentence.split(" ")
    words[0] = words[0].upper()
    for word in words:
        print(word)


def regex_thing(url_list, pattern):
    for url in url_list:
        if re.match(pattern, url):
            print("Matched.")
        else:
            print("Did not match.")


def main():
    # Format
    table_list = [("apple", 10, 0.7), ("banana", 28, 0.5), ("grape", 30, 0.1)]
    table_creator(table_list)

    # Some string methods
    splitter("These words will appear on a different line each time.")

    # Byte strings
    original_sentence = "This is thé 0riginal sentence. 頑張りましょう"
    print(original_sentence)
    byter = original_sentence.encode("UTF-8")
    print(byter)
    print(byter.decode("UTF-8"))

    # Byte array
    color_desc = "The color is orange"
    byte_desc = color_desc.encode("UTF-8")
    other_color = "purple"
    other_byte = other_color.encode("UTF-8")
    byte_arr = bytearray(byte_desc)
    print(byte_arr.decode("UTF-8"))
    byte_arr[13:19] = other_byte
    print(byte_arr.decode("UTF-8"))

    # regex
    url_good = "https://realpython.com/regex-python/"
    url_bad1 = "https:/realpython.com/regex-python/"
    url_bad2 = "https://realpythoncom/regex-python/"
    url_bad3 = "https://realpython.com/regex-python"
    url_bad4 = "https//realpython.com/regex-python/"
    url_bad5 = "https://realpython.com/regexpython/"
    pattern = "[a-z]{5}://[a-z]+\.[a-z]+/[a-z]+-[a-z]+/"
    regex_thing([url_good, url_bad1, url_bad2, url_bad3, url_bad4, url_bad5], pattern)


if __name__ == "__main__":
    main()
