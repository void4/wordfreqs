# this is a comment

# glob is a library that we import the glob function from
# The glob function returns a list of paths of all files in a directory
from glob import glob
# We use Counter objects to keep track of how many words there are of each stem
from collections import Counter
# We import the FrenchStemmer from the nltk library
from nltk.stem.snowball import FrenchStemmer

# First we get a list of file paths in the texts subfolder using the glob function
paths = glob("texts/*")

# We will add text from all files together in this variable
# In the beginning, it's just an empty string
text = ""

# Now we loop through all paths in the paths list
for path in paths:
	# The following line is executed for each path
	# We open the filepath and read its content
	# then add it to our 'text' variable
	text += open(path).read()

# These are the characters we will remove from our collected text
remove = ".,:[];-!?\"\'"

# For every character in the string above, we
for char in remove:
	# Replace the character in the text with an empty string (nothing)
	# the .replace() function returns the modified text,
	# so we assign that to our variable again
	text = text.replace(char, "")

# We create a FrenchStemmer object from the FrenchStemmer class and assign it to the variable name stemmer
# (a class is like a blueprint from which you can create infinite objects)
stemmer = FrenchStemmer()

# The same happens here, we create ('instantiate') a Counter object from the Counter class and name it 'counter'
counter = Counter()

# Now we split the text along its whitespace with the .split() function and loop over every word
for word in text.split():
	# We get the stem of the word using our 'stemmer' object, which has a .stem() function
	# Then, we assign the result of calling this function to the variable 'wordstem'
	wordstem = stemmer.stem(word)
	# We add one to the value associated with the wordstem key of our Counter
	counter[wordstem] += 1

# We sum all counter values together so we know how many words there are in total
totalwords = sum(counter.values())

# We output the total number of words to the console
# Strings starting with 'f' are format strings, they let us include expressions into the string
print(f"{totalwords} total words")

# We output the first row of our table
print("Count\tFreq.%\tWord")

# Now we loop over every key and value in our counter and name them 'word' and 'count' respectively
# ordered by highest value to lowest
for word, count in counter.most_common():
	# We create a string that indicates the frequency of this word, down to 2 commas
	# This is done by taking the word count, dividing it by the total number of words
	# and multiplying that by 100, to get a percentage value
	freq = "%.2f" % (count/totalwords*100)
	# Finally, we print the row for this word
	# Since this is a loop, this is done for every word key and count value in our counter
	print(f"{count}\t{freq}\t{word}")

# That's it for now :)
