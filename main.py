from controllers.auth_controller import AuthController
from views.auth_view import AuthView


def main():
    obj = AuthController()
    obj.initialize_interaction()


if __name__ == "__main__":
    main()