from abc import ABC, abstractmethod


class Calculator(ABC):

    @abstractmethod
    def addition(self, args):
        pass

    @abstractmethod
    def multiply(self, args):
        pass
