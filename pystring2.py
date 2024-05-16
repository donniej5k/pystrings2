#Task 1
def validate_name_length(first_name, last_name):
    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    if len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    if len(first_name) >= 2 and len(last_name) >= 2:
        print("Both names are valid.")

# Prompt user for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Validate the lengths
validate_name_length(first_name, last_name)

# Task 2
import re
password = input("Enter your password: ")
def check_password_complexity(password):
    # Check length
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return False

    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        print("Error: Password must contain at least one uppercase letter.")
        return False

    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        print("Error: Password must contain at least one lowercase letter.")
        return False

    # Check for digit
    if not re.search(r'[0-9]', password):
        print("Error: Password must contain at least one number.")
        return False

    print("Password meets complexity requirements.")
    return True


check_password_complexity(password)

#Task 3
def format_email(email):
    # Trim leading and trailing spaces
    email = email.strip()
    # Convert to lowercase
    email = email.lower()
    return email

email = input("Enter your email address: ")
formatted_email = format_email(email)
print(f"Formatted email address: {formatted_email}")

