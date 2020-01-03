from glob import glob
from nltk.stem.snowball import FrenchStemmer
from collections import Counter

paths = glob("texts/*")

text = ""

for path in paths:
	text += open(path).read()

remove = ".:[];-!?\"\'"

for char in remove:
	text = text.replace(char, "")

stemmer = FrenchStemmer()

counter = Counter()

for word in text.split():
	stem = stemmer.stem(word)
	counter[stem] += 1

totalwords = sum(counter.values())

print("Word\tCount\tRelative frequency (%)")

for word,count in counter.most_common():
	freq = "%.2f" % (count/totalwords*100)
	print(f"{count}\t{freq}\t{word}")
