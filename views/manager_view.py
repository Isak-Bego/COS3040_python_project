from utils.clear_console import clear_console
from views.base_view import BaseView

MAIN_MANAGER_TEMPLATE_SCREEN = \
"""
Hello {name}!

1. Manage Employees
2. Manage Menu Items
3. Manage Orders
4. Check Stats

5. Exit

Enter your choice (1 - 5): 
"""

EMPLOYEES_PAGE_HEADER = \
"""
Your employees:

"""

EMPLOYEE_CARD_TEMPLATE = \
"""
-----------------------------
Name: {name}
Surname: {surname}
Role: {role}
Passkey: {passkey}
-----------------------------
"""

EMPLOYEES_PAGE_MENU = \
"""
1. Add Employee
2. Edit Employee
3. Remove Employee

4. Exit

Enter your choice (1 - 4): 
"""

EMPLOYEES_EDIT_MENU = \
"""
1. Edit Name
2. Edit Surname
3. Edit Role

4. Exit
Enter your choice (1 - 4): 
"""

class ManagerView(BaseView):

    def __init__(self, manager):
        super().__init__()
        self.main_template_string = self.base_template_string + MAIN_MANAGER_TEMPLATE_SCREEN.format(name=manager["username"])

    def print_main_view(self):
        clear_console()
        print(self.main_template_string)

    def print_employees_view(self, employees):
        clear_console()
        print(EMPLOYEES_PAGE_HEADER)
        for employee in employees:
            name, surname, role, unique_passkey = employee
            print(EMPLOYEE_CARD_TEMPLATE.format(name=name, surname=surname, role=role, passkey=unique_passkey))
        print(EMPLOYEES_PAGE_MENU)

    def print_edit_view(self, employee):
        clear_console()
        print(EMPLOYEE_CARD_TEMPLATE.format(name=employee["name"], surname=employee["surname"], role=employee["role"], passkey=employee["unique_passkey"]))
        print(EMPLOYEES_EDIT_MENU)
