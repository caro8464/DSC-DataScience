import operator

# Load text from file
shakespeare_text = open("shakespeare.txt", "r")

# Read in text to string
strings = shakespeare_text.read()

# Split string into array of words
words = strings.split()

# Creating dictionary for word count
# Key => word itself
# Value => how many time the word is used
word_counts = dict()

# counting the words
for word in words:
	if word in word_counts:
		# if word already seen, we count plus 1 for the seen word
		word_counts[word] += 1
	else:
		# else the word is unseen its counter gets set to 1
		word_counts[word] = 1

# Sorting the dictionary by value and descending
# transformed to list for better extracting the 24th item
sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1),reverse=True)

# the last 24th item is the 24th most used word in the text
print(sorted_word_counts[23])