from controllers.base_controller import BaseController
from controllers.manager_controller import ManagerController
from models.managers_model import ManagerModel
from models.employee_model import EmployeeModel
from time import sleep
from views.auth_view import AuthView


class AuthController(BaseController):

    def __init__(self):
        self._auth_view = AuthView()
        self._manager_model = ManagerModel()
        self._employee_model = EmployeeModel()

    def initialize_interaction(self):
        choice = -1

        while choice != 4:

            self._auth_view.print_main_view()

            try:
                choice = int(input())
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            match choice:
                case 1:
                    result = self.authenticate_manager()
                    if result:
                        manager_controller = ManagerController(result)
                        manager_controller.initialize_interaction()
                case 2:
                    self.authenticate_cook()
                    # After the cooks is authenticated we pass the control to the respective controller
                case 3:
                    self.authenticate_server()
                    # After the server is authenticated we pass the control to the respective controller
                case 4:
                    print("Exiting...")
                case _:
                    print("Invalid choice. Please try again.")


    def authenticate_manager(self):
        username = ""
        while username != "q":
            self._auth_view.print_manager_login_view("username")
            # Get the user's input
            username = input()
            if username == "q": break
            # Fetch the data from the database
            user_credentials = self._manager_model.read(username=username)
            # Check if the user exists in the database
            if user_credentials:
                password = ""
                while password != "q":
                    self._auth_view.print_manager_login_view("password")
                    # Get the user's password
                    password = input()
                    if password == "q": break
                    # Check if the password is correct
                    if password == user_credentials["password"]:
                        return user_credentials
                    else:
                        print("Invalid password. Please try again.")
                        sleep(1)
            else:
                print("Invalid username. Please try again.")
                sleep(1)

        return None

    def authenticate_with_passkey(self, role):

        passkey = ""

        while passkey != "q":

            if role == "cook":
                self._auth_view.print_cook_login_view()
            else:
                self._auth_view.print_server_login_view()

            # Get the user's passkey
            passkey = input()

            if passkey == "q": break
            # Fetch the data from the database
            user_credentials = self._employee_model.read(passkey=passkey)
            # Verify if the user exists in the database and it matches its role
            if user_credentials and user_credentials["role"] == role:
                return user_credentials
            else:
                print("Invalid passkey. Please try again.")
                sleep(1)

        return None

    def authenticate_cook(self):
        self.authenticate_with_passkey("cook")

    def authenticate_server(self):
        self.authenticate_with_passkey("server")