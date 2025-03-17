# This program splits two sentences into sets and performs set operations.

# User input for sentences
sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")

# Creating sets of unique words
set1 = set(sentence1.lower().split())
set2 = set(sentence2.lower().split())

# Finding common words
common_words = set1.intersection(set2)

# Finding unique words in each sentence
unique_to_sentence1 = set1.difference(set2)
unique_to_sentence2 = set2.difference(set1)

# Displaying results
print("\nSet 1 (Unique words in Sentence 1):", set1)
print("Set 2 (Unique words in Sentence 2):", set2)
print("Common words in both sentences:", common_words)
print("Words unique to Sentence 1:", unique_to_sentence1)
print("Words unique to Sentence 2:", unique_to_sentence2)
