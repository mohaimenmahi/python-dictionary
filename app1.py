import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        print(data[w])
    elif len(get_close_matches(w, data.keys())) > 0:
        ex = get_close_matches(w, data.keys())[0]
        print("Did you mean %s instead? " % ex)
        ans = input("Y/N: ")
        if ans.lower() == 'y':
            print(data[ex])
        else:
            print("Try again!")
    else:
        return "The word doesn't exist."

word = input("Enter word: ")

translate(word)
