import re

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
