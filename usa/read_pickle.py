import pickle

with open("data/usa_share", "rb") as asd:
	a = pickle.load(asd)

print(a)
