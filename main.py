from controllers.auth_controller import AuthController

"""
This is the main entry point of the application. It creates an authenticationController instance and it calls the 
initialize_interaction() method.
"""

def main():
    obj = AuthController()
    obj.initialize_interaction()

if __name__ == "__main__":
    main()