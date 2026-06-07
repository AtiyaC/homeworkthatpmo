# Program to check if a character is an alphabet or not

# Get input from the user
char = input("Enter a character: ")

# Check if the input is a single character and an alphabet
if len(char) == 1 and char.isalpha():
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is NOT an alphabet.")
