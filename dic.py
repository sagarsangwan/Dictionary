import json
import difflib 
from difflib import get_close_matches, SequenceMatcher

data = json.load(open("data.json"))
def translate(word_lower):
    word_lower = word_lower.lower()
    if word_lower in data:
        return data[word_lower]
    elif len(get_close_matches(word_lower, data.keys(), ) )>0:
        yes_or_no = input("did u mean "+ '"'+( get_close_matches(word_lower, data.keys()) [0])+'"' +(" y for yes or n for no : "))
        yes_or_no = yes_or_no.lower()
        if yes_or_no == "y":
            return data[get_close_matches(word_lower, data.keys()) [0]] 
        if yes_or_no == "n":
            return "Please double check the word"
        else:
            return "Sorry we did't understand your entry"
    else:
        return "Please double check the word"
        
        
match_ratio = SequenceMatcher(None, "sagar", "sagrrr").ratio()
print(match_ratio)      


word = input("Enter a word: ")
output =translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print("enter valid word")
