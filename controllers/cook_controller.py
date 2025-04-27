from controllers.base_controller import BaseController
from models.order_items_model import OrderItemModel
from views.cook_view import CookView
from time import sleep


class CookController(BaseController):

    def __init__(self, cook):
        self._order_item_model = OrderItemModel()
        self._cook_view = CookView(cook)

    def initialize_interaction(self):
        order_items = self._order_item_model.read_all()
        self._cook_view.print_cook_view(order_items)

        choice = ""
        while choice != "q":
            choice = input("Press q to exit...")


