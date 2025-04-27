from utils.clear_console import clear_console
from views.order_view import OrderView

"""
This module is responsible for constructing and managing the server view.
"""

SERVER_MAIN_SCREEN = \
"""
Hello {name}!
Here are your active orders:
"""

class ServerView(OrderView):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def print_server_view(self):
        clear_console()
        print(SERVER_MAIN_SCREEN.format(name=self.server["name"]))