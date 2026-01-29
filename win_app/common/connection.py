from abc import ABC, abstractmethod

class Connection(ABC):
           
    @abstractmethod
    def get_type(self) -> str:
        pass
    
    @abstractmethod
    def get_id(self) -> str:
        pass
    
    @abstractmethod
    def _verify(self) -> bool:
        pass