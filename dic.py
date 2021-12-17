import json
import difflib 
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
def translate(word_lower):
        
    word_lower = word_lower.lower()
    if word_lower in data:
        return data[word_lower]
   
   
word = input("enter a word: ")
output =translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print("enter valid word")
