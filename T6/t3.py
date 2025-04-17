def remove_whitespace(text):
    return text.replace(" ", "")

# Get input from the user
input_text = input("Enter a string: ")

# Process and display the result
output_text = remove_whitespace(input_text)
print("String without whitespace:", output_text)