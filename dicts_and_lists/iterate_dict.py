my_dict = {
    "Name": "Thomas",
    "Age": 25,
    "Sex": "Male"
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key, my_dict[key]

# Iterating over a dictionary
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print movies.items()