# 1. Print the multiple of 5 in a list using map and filter 
numbers = list(range(1, 51))
def is_multiple_of_5(number):
    return number % 5 == 0
filtered_numbers = filter(is_multiple_of_5, numbers)
multiples_of_5 = list(filtered_numbers)
print("Multiples of 5 from 1 to 50:")
print(multiples_of_5)

# output:-
# Multiples of 5 from 1 to 50:
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# 2. Print the vowels in the string using map and filter
input_string = "Hello World, Python is Amazing"
def is_vowel(character):
    return character in 'aeiouAEIOU'
characters = list(input_string)
filtered_vowels = filter(is_vowel, characters)
vowel_list = list(filtered_vowels)
print("Vowels in the string:")
print(vowel_list)

# output:-
# Vowels in the string:
# ['e', 'o', 'o', 'o', 'i', 'A', 'a', 'i']
