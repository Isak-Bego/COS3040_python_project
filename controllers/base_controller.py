from abc import ABC, abstractmethod


class BaseController(ABC):

    @abstractmethod
    def initialize_interaction(self):
        pass

