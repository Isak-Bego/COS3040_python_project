from utils.clear_console import clear_console
from views.base_view import BaseView

MAIN_AUTH_TEMPLATE_STRING = \
"""
Login as: 

    1. Manager
    2. Cook 
    3. Server
    
    4. Exit

Enter your choice (1 - 4): 
"""

LOGIN_HEADER_TEMPLATE = \
"""
===========================================
              {role} LOGIN
===========================================
"""

MANAGER_LOGIN_CREDENTIAL_TEMPLATE = \
"""
Enter {credential}: 
"""

PASSCODE_LOGIN_VIEW = \
"""
Enter passcode:
"""

class AuthView(BaseView):

    def __init__(self):
        super().__init__()
        self.main_template_string = self.base_template_string + MAIN_AUTH_TEMPLATE_STRING

    def print_main_view(self):
        clear_console()
        print(self.main_template_string)

    def print_manager_login_view(self, chosen_view):
        match chosen_view:
            case 'username':
                clear_console()
                print(LOGIN_HEADER_TEMPLATE.format(role='MANAGER'))
                print(MANAGER_LOGIN_CREDENTIAL_TEMPLATE.format(credential=chosen_view))
            case 'password':
                clear_console()
                print(LOGIN_HEADER_TEMPLATE.format(role='MANAGER'))
                print(MANAGER_LOGIN_CREDENTIAL_TEMPLATE.format(credential=chosen_view))


    def print_server_login_view(self):
        clear_console()
        print(LOGIN_HEADER_TEMPLATE.format(role='SERVER'))
        print(PASSCODE_LOGIN_VIEW)

    def print_cook_login_view(self):
        clear_console()
        print(LOGIN_HEADER_TEMPLATE.format(role='COOK'))
        print(PASSCODE_LOGIN_VIEW)
