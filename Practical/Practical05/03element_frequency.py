# This program counts the frequency of elements in a list with and without using count().

def frequency_with_count(lst):
    freq_dict = {}
    for item in lst:
        freq_dict[item] = lst.count(item)
    return freq_dict

def frequency_without_count(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

# Input list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Frequency calculations
freq_using_count = frequency_with_count(numbers)
freq_without_count = frequency_without_count(numbers)

print("Original List:", numbers)
print("Frequency (Using count()):", freq_using_count)
print("Frequency (Without count()):", freq_without_count)

