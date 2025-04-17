def count_words_of_length(text, m):
    words = text.split()
    count = sum(1 for word in words if len(word) == m)
    return count

# Get input
text = input("Enter a string: ")
m = int(input("Enter word length (m): "))

# Call function
result = count_words_of_length(text, m)
print(f"Number of words with length {m}: {result}")