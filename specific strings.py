#Writing a program that searches for a specific string within a list of strings.
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]# Initializing the list of names

# Prompt user for input
search_term = input("Enter the name you want to search for: ")

# Searching for the term in the list
if search_term in names:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")