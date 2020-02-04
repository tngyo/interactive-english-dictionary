import json
import difflib

data = json.load(open("data.json"))


def define(word):
    closest_match = difflib.get_close_matches(word, data.keys(), 1)
    if closest_match:
        closest = closest_match[0]
        match_ratio = ratio(word, closest)
        if match_ratio < 100:
            if ratio(word.capitalize(), closest) == 100:
                return prettify(data[closest], closest)
            user_input = input("\nDo you mean %s instead? Press Y or N: " % closest)
            if user_input == 'Y':
                print(f'\n**The match ratio for {word} and {closest} is: {match_ratio} percent**')
                return prettify(data[closest], closest)
            elif user_input == 'N':
                return "\nSorry, %s was not found in this dictionary.\n" % word
            else:
                return "\nSorry this input is not understood.\n"
        return prettify(data[closest], closest)
    else:
        return "\nSorry, %s is not found in this dictionary.\n" % word


def ratio(word, closest):
    match_ratio = difflib.SequenceMatcher(None, word, closest).ratio()
    return round(match_ratio, 2) * 100


def prettify(list, closest):
    print(f"\n{closest}\n")
    for numbering, line in enumerate(list):
        print(f'\n{numbering+1}. {line}')
    return "\nDone! Thank you for learning English :-)\n"


if __name__ == "__main__":
    word = input("\n\nEnter a word for definition: ")
    print(define(word.lower()))
