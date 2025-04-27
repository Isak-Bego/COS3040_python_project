from abc import ABC, abstractmethod

"""
This is an abstract method for the controllers. Every controller has to have an entrypoint that is called by the 
authenticator instance. This entrypoint is called initialize_interaction()
"""

class BaseController(ABC):

    @abstractmethod
    def initialize_interaction(self, *args, **kwargs):
        pass

