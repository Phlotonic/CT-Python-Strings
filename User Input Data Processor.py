# Task 1: Input Length Validator
# This script asks for and checks the length of the user's 
# first name and last name.
# Both should be at least 2 characters long. If not, it 
# prints an error message.

# Function to validate the length of the input
def validate_name_length(name):
    # Check if the length of the name is at least 2 characters
    if len(name) < 2:
        return False
    return True

# Ask the user for their first name
first_name = input("Enter your first name: ")

# Ask the user for their last name
last_name = input("Enter your last name: ")

# Validate the length of the first name
if not validate_name_length(first_name):
    print("Error: First name must be at least 2 characters long.")

# Validate the length of the last name
if not validate_name_length(last_name):
    print("Error: Last name must be at least 2 characters long.")

# If both names are valid, print a success message
if validate_name_length(first_name) and validate_name_length(last_name):
    print("Both names are valid.")
