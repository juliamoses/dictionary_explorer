import json

# app.py is opening & reading dictionary data
data = json.load(open("data.json"))

# returns definition of word
def translate(w):
	w = w.lower()
	# if the word is in json dictionary, will give definition
	if w in data:
		return data[w]
	else:
		return "Sorry! this word isn't in the dictionary, please double check it."

word = input("Enter a word: ")

print(translate(word))