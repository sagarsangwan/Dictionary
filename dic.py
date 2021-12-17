import json
import difflib 
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
print(data.keys())
