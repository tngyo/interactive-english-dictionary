import json
import difflib

data = json.load(open("data.json"))


def define(word):
    closest_match = difflib.get_close_matches(word, data.keys(), 1)
    if closest_match:
        match_ratio = difflib.SequenceMatcher(None, word, closest_match[0]).ratio()
        match_ratio = round(match_ratio, 2) * 100
        if match_ratio < 100:
            user_input = input("\nDo you mean %s instead? Press Y or N: " % closest_match[0].upper())
            if user_input == 'Y':
                print(f'\nMatch ratio for {word} and {closest_match[0]} is: {match_ratio} percent')
                print(f"\n{closest_match[0]}\n")
                return prettify(data[closest_match[0]])
            elif user_input == 'N':
                return "\nSorry word was not found in this dictionary.\n"
            else:
                return "\nSorry this input is not understood.\n"
        return prettify(data[closest_match[0]])
    else:
        return "\nSorry, {word} is not found in this dictionary.\n"


def prettify(list):
    numbering = 1
    for line in list:
        print(f'\n{numbering}. {line}')
        numbering += 1
    return "\nDone! Thank you for learning English :-)\n"


if __name__ == "__main__":
    word = input("\n\nEnter a word for definition: ")
    print(define(word.lower()))
