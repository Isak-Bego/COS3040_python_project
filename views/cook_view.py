from utils.clear_console import clear_console
from views.order_view import OrderView

"""
This module is responsible for constructing and managing the cook view.
"""

COOK_MAIN_SCREEN = \
"""
Hello {name}!
Here is the stuff that you have to prepare. Good luck!

"""

class CookView(OrderView):
    def __init__(self, cook):
        super().__init__()
        self.cook = cook

    def print_cook_view(self, order_items):
        clear_console()
        print(COOK_MAIN_SCREEN.format(name=self.cook["name"]))
        # Filter all the order items that are not prepared
        uprepared_order_items = [order_item for order_item in order_items if order_item[3] == "False"]
        self.print_all_order_items(uprepared_order_items)
