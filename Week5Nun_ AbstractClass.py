from abc import ABC, abstractmethod

class Shape(ABC):
    '''A class representing a geometrical shape'''
    def __init__(self, id):
        self.id = id

    def name(self):
        return self.id

    @abstractmethod
    def area (self):
        pass

    @abstractmethod
    def perimeter(self)
        pass

    @abstractmethod
    def
