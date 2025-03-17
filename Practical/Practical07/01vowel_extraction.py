# This program extracts vowels from a given sentence and returns them as a set.

def extract_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return {char for char in sentence if char in vowels}

# User input
sentence = input("Enter a sentence: ")
vowel_set = extract_vowels(sentence)

print("Vowels present in the sentence:", vowel_set)
