text = input("Enter a string ending with '.': ").rstrip('.')
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")