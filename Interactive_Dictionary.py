import json
from difflib import get_close_matches


data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        sc=input("Did you mean %s Y for yes and N for no" %get_close_matches(w,data.keys())[0])
        if sc=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            print("No matches")
    else:
        print("Not available")

word=input("Enter the word: ")
print (translate(word))
