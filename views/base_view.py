from abc import ABC, abstractmethod

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
