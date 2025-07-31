string = input("Enter a string: ")

# Dictionary to store character counts
char_count = {}

# Count occurrences of each character in the string
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print duplicate characters along with their counts
print("Duplicate characters and their counts:")
for char, count in char_count.items():
    if count > 1:
        print(f"'{char}' appeared {count} times.")            