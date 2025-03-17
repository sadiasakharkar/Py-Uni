# Step 1: Input sentences
sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")

# Step 2: Split into words and create sets
set1 = set(sentence1.lower().split())  # Convert to lowercase & split into words
set2 = set(sentence2.lower().split())  # Convert to lowercase & split into words

# Step 3: Find common words
common_words = set1.intersection(set2)

# Step 4: Find words unique to each sentence
unique_to_sentence1 = set1.difference(set2)  # Words in set1 but not in set2
unique_to_sentence2 = set2.difference(set1)  # Words in set2 but not in set1

# Display results
print("\nSet of unique words in sentence 1:", set1)
print("Set of unique words in sentence 2:", set2)
print("Common words in both sentences:", common_words)
print("Words unique to sentence 1:", unique_to_sentence1)
print("Words unique to sentence 2:", unique_to_sentence2)
