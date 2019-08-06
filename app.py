import json
from difflib import get_close_matches

# app.py is opening & reading dictionary data
data = json.load(open("data.json"))

# returns definition of word
def translate(w):
	w = w.lower()
	# if the word is in json dictionary, will give definition
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
		y = input("Do you mean %s instead? Press Press y if yes, and n if no: " 
			% get_close_matches(w, data.keys())[0])
		if y == "y":
			return data[get_close_matches(w, data.keys())[0]]
		elif y == "n":
			return "Sorry! this word isn't in the dictionary, please double check it."
		else:
			return "Sorry! please enter y or n"
	else:
		return "Sorry! this word isn't in the dictionary, please double check it."

word = input("Enter a word: ")

print(translate(word))