from controllers.base_controller import BaseController
from models.menu_items_model import MenuItemModel
from models.order_items_model import OrderItemModel
from utils.get_unique_order import get_unique_orders
from views.order_view import OrderView

"""
Here is located the logic behind the order management.
"""

class OrderController(BaseController):
    def __init__(self):
        self._menu_items_model = MenuItemModel()
        self._order_view = OrderView()
        self._order_items_model = OrderItemModel()


    def initialize_interaction(self, order_items):
        choice = -1

        while choice != 3:
            unique_orders = get_unique_orders(order_items)
            self._order_view.print_main_view(unique_orders)

            try:
                choice = int(input())

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            match choice:
                case 1:
                    order_items = self.create_new_order()
                case 2:
                    order_items = self.edit_existing_order()
                case 3:
                    print("Exiting...")
                case _:
                    print("Invalid choice. Please try again.")

    def create_new_order(self):
        menu_items = self._menu_items_model.read_all()
        self._order_view.print_new_order_view(menu_items)

        item_id = int(input("Enter item id: "))
        item_quantity = int(input("Enter item quantity: "))
        self._order_items_model.create(item_id=item_id, quantity=item_quantity)
        return self._order_items_model.read_all()

    def edit_existing_order(self):
        menu_items = self._menu_items_model.read_all()
        order_items = self._order_items_model.read_all()
        order_id = input("Enter order ID: ")

        self._order_view.print_existing_order_view(order_id=order_id, menu_items=menu_items, order_items=order_items)

        choice = -1

        while choice != 3:
            try:
                choice = int(input())

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            match choice:
                case 1:
                    item_id = int(input("Enter item id: "))
                    item_quantity = int(input("Enter item quantity: "))
                    self._order_items_model.create(order_id=order_id, item_id=item_id, quantity=item_quantity)
                    return self._order_items_model.read_all()
                case 2:
                    item_id = int(input("Enter item id: "))
                    self._order_items_model.delete(order_id=order_id, item_id=item_id)
                    return self._order_items_model.read_all()
                case 3:
                    print("Exiting...")
                    return order_items
                case _:
                    print("Invalid choice. Please try again.")