def capitalize_first_letters(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Get input from the user
input_text = input("Enter a string: ")

# Process and display the result
output_text = capitalize_first_letters(input_text)
print("String after capitalization:", output_text)