import os

"""
This is a utility function for clearing the console.
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')