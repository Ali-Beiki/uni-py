def count_substring(main_string, sub_string):
    count = 0
    len_sub = len(sub_string)
    for i in range(len(main_string) - len_sub + 1):
        if main_string[i:i+len_sub] == sub_string:
            count += 1
    return count

# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function and display the result
result = count_substring(string2, string1)
print(f"The first string appears {result} times in the second string.")