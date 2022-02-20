
from abc import ABC , abstractmethod


class Person(ABC):
    @abstractmethod
    def speaking() -> None :
        pass
    
    @abstractmethod
    def walking() -> None:
        pass

class Jaeyong(Person):
    def speaking() -> None:
        "Jaeyong이는 달린다"
    

def main() -> None:
    jy = Jaeyong()
    jy.speaking()

if __name__ == '__main__':
    main()