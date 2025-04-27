from abc import ABC, abstractmethod

"""
This is the base view module which defines the header of the application but also defines an abstract method
that is implemented by all the other views.
"""


SYSTEM_HEADER = \
"""
===========================================
       RESTAURANT MANAGEMENT SYSTEM
===========================================
"""

class BaseView(ABC):

    def __init__(self):
        self.base_template_string = SYSTEM_HEADER

    @abstractmethod
    def print_main_view(self, *args, **kwargs):
        pass
