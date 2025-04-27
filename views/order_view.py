from utils.clear_console import clear_console
from views.base_view import BaseView
from views.manager_view import MENU_ITEM_TEMPLATE

"""
This module is responsible for constructing and managing the order view.
"""

ORDER_ITEM_TEMPLATE = \
"""
-----------------------------
id: {id}
quantity: {quantity}
prepared: {prepared}
-----------------------------
"""

MANAGE_ORDER_MENU = \
"""
1. Create new order
2. Modify existing order

3. Exit
Enter your choice (1 - 3):
"""

EDIT_ORDER_MENU = \
"""
1. Add Item
2. Remove Item

3. Exit
Enter your choice (1 - 3):
"""

class OrderView(BaseView):

    def print_main_view(self, order_item_ids):
        clear_console()
        print("Orders: ")
        for order_item_id in order_item_ids:
            print("id", order_item_id)
        print(MANAGE_ORDER_MENU)

    def print_new_order_view(self, menu_items):
        clear_console()
        for menu_item in menu_items:
            id, name, category, price = menu_item
            print(MENU_ITEM_TEMPLATE.format(id=id, name=name, category=category, price=price))

    def print_all_order_items(self, order_items):
        for order_item in order_items:
            order_id, item_id, quantity, preparation_status = order_item
            print(ORDER_ITEM_TEMPLATE.format(id=item_id, quantity=quantity, prepared=preparation_status))

    def print_existing_order_view(self, order_id, menu_items, order_items):
        print(f"Order id:{order_id}: ")
        print(f"Avaliable menu items: ")
        for menu_item in menu_items :
            id, name, category, price = menu_item
            print(MENU_ITEM_TEMPLATE.format(id=id, name=name, category=category, price=price))

        # Filter the items with this order id:
        this_order_items = [order_item for order_item in order_items if order_item[0] == order_id]

        print(f"Items on this order: ")
        for order_item in this_order_items:
            order_id, item_id, quantity, preparation_status = order_item
            print(ORDER_ITEM_TEMPLATE.format(id=item_id, quantity=quantity, prepared=preparation_status))

        print(EDIT_ORDER_MENU)