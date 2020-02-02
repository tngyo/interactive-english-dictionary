import json
import difflib

data = json.load(open("data.json"))


def define(word):
    closest_match = difflib.get_close_matches(word, data.keys(), 1)
    if closest_match:
        print(f"\n{closest_match[0]}")
        prettify(data[closest_match[0]])
    else:
        print(f"\nSorry, {word} is not found in this dictionary.\n")
        

"""
    try:
        prettify(data[word])
    except KeyError:
        print("\nThis word is not defined in this local dictionary.\n")
"""


def prettify(list):
    numbering = 1
    for line in list:
        print(f'\n{numbering}. {line}')
        numbering += 1
    print("\nDone! Thank you for learning English :-)\n")


if __name__ == "__main__":
    word = input("\n\nEnter a word for definition: ")
    define(word.lower())
