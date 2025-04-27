from controllers.order_controller import OrderController
from models.order_items_model import OrderItemModel
from views.server_view import ServerView


class ServerController(OrderController):
    def __init__(self, server):
        super().__init__()
        self.server = server
        self._server_view = ServerView(server)
        self._order_items_model = OrderItemModel()

    def open_server_interface(self):
        self._server_view.print_server_view()
        order_items = self._order_items_model.read_all()
        self.initialize_interaction(order_items)