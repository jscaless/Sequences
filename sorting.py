pangram = "The quick brown fox jumps over the lazy dog"
pangram2 = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

sorted_pangram = sorted(pangram) # Gives all items within the order.
sorted_pangram2 = sorted(pangram2, key=str.casefold) # The key=str casefold is for case-insenstive sorting
print(sorted_pangram)
print(sorted_pangram2)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumps  over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Alexes",
         "Jyotsna",
         "Joshua",
         "eric",
         "terry"]
names.sort(key=str.casefold)
print(names)
