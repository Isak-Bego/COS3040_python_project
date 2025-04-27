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

MANAGE_PAGE_MENU = \
"""
1. Add {item}
2. Edit {item}
3. Remove {item}

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

MENU_ITEM_EDIT_MENU = \
"""
1. Edit Name
2. Edit Category
3. Edit Price

4. Exit
Enter your choice (1 - 4): 
"""

MENU_ITEM_TEMPLATE = \
"""
-----------------------------
Id: {id}
name: {name}
category: {category}
price: {price}
-----------------------------
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
        print(MANAGE_PAGE_MENU.format(item="Employee"))

    def print_employee_edit_view(self, employee):
        clear_console()
        print(EMPLOYEE_CARD_TEMPLATE.format(name=employee["name"], surname=employee["surname"], role=employee["role"], passkey=employee["unique_passkey"]))
        print(EMPLOYEES_EDIT_MENU)

    def print_menu_item_edit_view(self, menu_item):
        clear_console()
        print(MENU_ITEM_TEMPLATE.format(id=menu_item["id"], name=menu_item["name"], category=menu_item["category"], price=menu_item["price"]))
        print(MENU_ITEM_EDIT_MENU)

    def print_menu_items_view(self, menu_items):
        clear_console()
        for menu_item in menu_items:
            id, name, category, price = menu_item
            print(MENU_ITEM_TEMPLATE.format(id=id, name=name, category=category, price=price))
        print(MANAGE_PAGE_MENU.format(item="Menu Item"))
