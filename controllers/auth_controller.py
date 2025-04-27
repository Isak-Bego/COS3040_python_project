from controllers.base_controller import BaseController
from views.auth_view import AuthView


class AuthController(BaseController):

    def __init__(self):
        self._auth_view = AuthView()

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
                    self.authenticate_manager()
                case 2:
                    self.authenticate_cook()
                case 3:
                    self.authenticate_server()
                case 4:
                    print("Exiting...")
                case _:
                    print("Invalid choice. Please try again.")


    def authenticate_manager(self):
        self._auth_view.print_manager_login_view("username")
        self._auth_view.print_manager_login_view("password")

    def authenticate_cook(self):
        self._auth_view.print_cook_login_view()

    def authenticate_server(self):
        self._auth_view.print_server_login_view()