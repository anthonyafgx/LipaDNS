from abc import ABC, abstractmethod

class IPInterface(ABC):
    @property
    def previous_ipv4(self) -> str:
        return self._previous_ipv4
    
    @previous_ipv4.setter
    def previous_ipv4(self, value: str) -> None:
        self._previous_ipv4 = value

    @abstractmethod
    def scan_ipv4(self) -> str:
        return
    
    @abstractmethod
    def scan_ipv6(self) -> str:
        return