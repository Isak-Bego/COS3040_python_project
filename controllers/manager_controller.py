from controllers.base_controller import BaseController
from controllers.order_controller import OrderController
from models.employee_model import EmployeeModel
from models.menu_items_model import MenuItemModel
from models.order_items_model import OrderItemModel
from utils.validations import validate_name, validate_surname, validate_role, validate_passkey, get_valid_input, \
    validate_category, validate_price
from views.manager_view import ManagerView

from views.order_view import OrderView


class ManagerController(BaseController):

    def __init__(self, manager):
        self._manager_view = ManagerView(manager)
        self._employee_model = EmployeeModel()
        self._menu_items_model = MenuItemModel()
        self._order_items_model = OrderItemModel()
        self._order_view = OrderView()
        self._order_controller = OrderController()

    def initialize_interaction(self):
        choice = -1

        while choice != 4:

            self._manager_view.print_main_view()

            try:
                choice = int(input())

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            match choice:
                case 1:
                    employees = self._employee_model.read_all()
                    self.manage_employees(employees)
                case 2:
                    menu_items = self._menu_items_model.read_all()
                    self.manage_menu_items(menu_items)
                case 3:
                    order_items = self._order_items_model.read_all()
                    self._order_controller.initialize_interaction(order_items)
                case 4:
                    print("Exiting...")
                case _:
                    print("Invalid choice. Please try again.")


    def manage_employees(self, employees):
        choice = -1

        while choice != 4:

            self._manager_view.print_employees_view(employees)

            try:
                choice = int(input())

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            match choice:
                case 1:
                    employees = self.add_employee()
                case 2:
                    employees = self.edit_employee()
                case 3:
                    employees = self.remove_employee()
                case 4:
                    print("Exiting...")
                case _:
                    print("Invalid choice. Please try again.")

    def add_employee(self):
        """Add an employee after validating input fields."""
        employee_name = get_valid_input("Enter employee name: ", validate_name)
        employee_surname = get_valid_input("Enter employee surname: ", validate_surname)
        employee_role = get_valid_input("Enter employee role: ", validate_role)
        employee_passcode = get_valid_input("Enter employee passcode: ", validate_passkey)

        self._employee_model.create(employee_name, employee_surname, employee_role, employee_passcode)
        return self._employee_model.read_all()

    def edit_employee(self):
        employee_passcode = get_valid_input("Enter employee passcode: ", validate_passkey)
        employee = self._employee_model.read(employee_passcode)

        while (not employee):
            print("Invalid passcode. Please try again.")
            employee_passcode = get_valid_input("Enter employee passcode: ", validate_passkey)
            employee = self._employee_model.read(employee_passcode)

        self._manager_view.print_employee_edit_view(employee)
        choice = int(input())

        match choice:
            case 1:
                # Edit Name
                new_name = get_valid_input("Enter new employee name: ", validate_name)
                self._employee_model.update(employee["unique_passkey"], new_name=new_name)
            case 2:
                # Edit Surname
                new_surname = get_valid_input("Enter new employee surname: ", validate_surname)
                self._employee_model.update(employee["unique_passkey"], new_surname=new_surname)
            case 3:
                # Edit Role
                new_role = get_valid_input("Enter new employee role: ", validate_role)
                self._employee_model.update(employee["unique_passkey"], new_role=new_role)

        return self._employee_model.read_all()


    def remove_employee(self):
        employee_passcode = get_valid_input("Enter employee passcode: ", validate_passkey)
        employee = self._employee_model.read(employee_passcode)

        while (not employee):
            print("Invalid passcode. Please try again.")
            employee_passcode = get_valid_input("Enter employee passcode: ", validate_passkey)
            employee = self._employee_model.read(employee_passcode)

        self._employee_model.delete(employee["unique_passkey"])
        return self._employee_model.read_all()

    def manage_menu_items(self, menu_items):
        choice = -1

        while choice != 4:

            self._manager_view.print_menu_items_view(menu_items)

            try:
                choice = int(input())

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            match choice:
                case 1:
                    menu_items = self.add_menu_item()
                case 2:
                    menu_items = self.edit_menu_item()
                case 3:
                    menu_items = self.remove_menu_item()
                case 4:
                    print("Exiting...")
                case _:
                    print("Invalid choice. Please try again.")


    def add_menu_item(self):
        """Add a menu_item after validating input fields."""
        item_name = get_valid_input("Enter menu item name: ", validate_name)
        item_category = get_valid_input("Enter menu item category: ", validate_category)
        item_price = get_valid_input("Enter menu item price: ", validate_price)

        self._menu_items_model.create(item_name, item_category, item_price)
        return self._menu_items_model.read_all()

    def edit_menu_item(self):
        menu_item_id = int(input("Enter menu item id: "))
        menu_item = self._menu_items_model.read(menu_item_id)

        while (not menu_item):
            print("Invalid menu item ID. Please try again.")
            menu_item_id = int(input("Enter menu item id: "))
            menu_item = self._menu_items_model.read(menu_item_id)

        self._manager_view.print_menu_item_edit_view(menu_item)
        choice = int(input())

        match choice:
            case 1:
                # Edit Name
                new_name = get_valid_input("Enter new menu item name: ", validate_name)
                self._menu_items_model.update(menu_item["id"], new_name=new_name)
            case 2:
                # Edit Category
                new_category = get_valid_input("Enter new menu item category: ", validate_category)
                self._menu_items_model.update(menu_item["category"], new_category=new_category)
            case 3:
                # Edit Price
                new_price = get_valid_input("Enter new menu item price: ", validate_price)
                self._menu_items_model.update(menu_item["price"], new_price=new_price)

        return self._menu_items_model.read_all()

    def remove_menu_item(self):
        menu_item_id = int(input("Enter menu item id: "))
        menu_item = self._menu_items_model.read(menu_item_id)

        while (not menu_item):
            print("Invalid menu item id. Please try again.")
            menu_item_id = int(input("Enter menu item id: "))
            menu_item = self._menu_items_model.read(menu_item_id)

        self._menu_items_model.delete(menu_item["id"])
        return self._menu_items_model.read_all()