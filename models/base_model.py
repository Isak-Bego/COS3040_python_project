from abc import ABC, abstractmethod

"""
This module contains the abstract methods of the Models. It serves as an interface for all the models. 
"""

class BaseModel(ABC):

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def read(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass
