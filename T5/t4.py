def separate_numbers():
    # Initialize lists
    all_numbers = []
    positive_numbers = []
    negative_numbers = []
    
    # Input numbers
    print("Enter integers (positive and negative). Enter 'done' when finished:")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break
        try:
            num = int(user_input)
            all_numbers.append(num)
        except ValueError:
            print("Please enter a valid integer or 'done' to finish.")
    
    # Separate numbers
    for num in all_numbers:
        if num >= 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)
    
    # Display results
    print("\nOriginal list:", all_numbers)
    print("Positive numbers:", positive_numbers)
    print("Negative numbers:", negative_numbers)

# Run the program
separate_numbers()