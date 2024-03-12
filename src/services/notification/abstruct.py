from abc import ABC, abstractmethod


class AbstractNotify(ABC):
    @abstractmethod
    def send_message(self, message: str) -> str:
        raise NotImplementedError()