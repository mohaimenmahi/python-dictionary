import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        ex = get_close_matches(w, data.keys())[0]
        return "Did you mean %s instead? " % ex
        ans = input("Y/N: ")
        if ans.lower() == 'y':
            return data[ex]
        else:
            return "Try again!"
    else:
        return "The word doesn't exist."

word = input("Enter word: ")

ans = translate(word)

for item in ans:
    print(item)
