from controllers.base_controller import BaseController
from models.employee_model import EmployeeModel
from utils.validations import validate_name, validate_surname, validate_role, validate_passkey, get_valid_input
from views.manager_view import ManagerView
from time import sleep


class ManagerController(BaseController):

    def __init__(self, manager):
        self._manager_view = ManagerView(manager)
        self._employee_model = EmployeeModel()

    def initialize_interaction(self):
        choice = -1

        while choice != 5:

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
                    print("2")
                case 3:
                    print("3")
                case 4:
                    print("4")
                case 5:
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

        self._manager_view.print_edit_view(employee)
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