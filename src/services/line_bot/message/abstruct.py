from abc import ABC, abstractmethod


class AbstractLineMessage(ABC):
    @abstractmethod
    def builder(self):
        raise NotImplementedError()