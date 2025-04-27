import re

"""
This module contains validator functions using regular expressions.
"""

def get_valid_input(prompt, validator_func):
    """Helper function to get validated input."""
    user_input = input(prompt)
    while not validator_func(user_input):
        user_input = input(prompt)
    return user_input

def validate_name(name: str) -> bool:
    """Validates that the name contains only letters (A-Z, a-z)."""
    pattern = r'^[A-Za-z]+$'
    if(not bool(re.match(pattern, name))):
        print("Error: The name should only contain letters (A-Z, a-z).")
        return False

    return True

def validate_surname(surname: str) -> bool:
    """Validates that the surname contains only letters (A-Z, a-z)."""
    pattern = r'^[A-Za-z]+$'
    if not bool(re.match(pattern, surname)):
        print("Error: The surname should only contain letters (A-Z, a-z).")
        return False

    return True

def validate_role(role: str) -> bool:
    """Validates that the role is either 'cook' or 'server'"""
    pattern = r'^(cook|server)$'
    if not bool(re.match(pattern, role)):
        print("Error: The role should either be 'cook' or 'server'.")
        return False
    return True

def validate_passkey(passkey: str) -> bool:
    """Validates that the passkey is exactly 4 digits."""
    pattern = r'^\d{4}$'
    if not bool(re.match(pattern, passkey)):
        print("Error: The passkey should only 4 digits.")
        return False
    return True

def validate_price(price: str) -> bool:
    """Validates that the price is a positive number."""
    pattern = r'^\d+(\.\d{1,2})?$'  # Matches positive numbers with up to two decimal places
    if not bool(re.match(pattern, price)):
        print("Error: The price should be a positive number, with up to two decimal places.")
        return False
    return True

def validate_category(category: str) -> bool:
    """Validates that the category is either 'cocktails', 'deserts', or 'main_course'."""
    pattern = r'^(cocktails|deserts|main_course)$'
    if not bool(re.match(pattern, category)):
        print("Error: The category should be either 'cocktails', 'deserts', or 'main_course'.")
        return False
    return True

def validate_integer(value: str) -> bool:
    """Validates that the value is a valid integer."""
    pattern = r'^[-+]?\d+$'  # Matches optional + or - followed by digits
    if not bool(re.match(pattern, value)):
        print("Error: The value should be a valid integer.")
        return False
    return True


