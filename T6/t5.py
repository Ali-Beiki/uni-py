my_dictionary = {
    "apple": "a fruit",
    "code": "instructions for a computer",
    "python": "a programming language"
}

def manage_dictionary():
    while True:
        print("\n1. Add word\n2. Lookup word\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            word = input("Enter word: ")
            meaning = input("Enter meaning: ")
            my_dictionary[word] = meaning
            print("Word added!")
        
        elif choice == "2":
            word = input("Enter word to lookup: ")
            print(f"Meaning: {my_dictionary.get(word, 'Word not found')}")
        
        elif choice == "3":
            break

manage_dictionary()