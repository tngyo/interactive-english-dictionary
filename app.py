import json


data = json.load(open("data.json"))


def define(word):
    if word in data:
        prettify(data[word])
    else:
        print("\nSorry. Word is not found in this dictionary.\n")

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
