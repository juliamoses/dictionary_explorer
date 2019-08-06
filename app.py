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
	elif w.title() in data: #"texas" checks for "Texas" 
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]

	elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
		y = input("Do you mean %s instead? Press Press y if yes, and n if no: " 
			% get_close_matches(w, data.keys())[0])
		if y == "y":
			return data[get_close_matches(w, data.keys())[0]]
		elif y == "n":
			return "Sorry! we couldn't find your word in the dictionary, please double check it."
		else:
			return "Sorry! please enter y or n"
	else:
		return "Sorry! this word isn't in the dictionary, please double check it."

word = input("Enter a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)