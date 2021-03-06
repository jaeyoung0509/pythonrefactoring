
from abc import ABC , abstractmethod


class Simian(ABC):
    @abstractmethod
    def walking(self) -> None:
        pass


class Human(Simian):
    @abstractmethod
    def speaking(self) -> None :
        pass
    
class Monkey(Simian):
    def walking(self) -> None:
        print(
            f"{type(self)} is walking" 
            )       
class Jaeyong(Human):
    def speaking(self) -> None:
        print(
            f"{type(self)} is speaking" 
            )
    def walking(self) -> None:
        print(
            f"{type(self)} is walking" 
            )


class BeSimian:
    def be(self , obj : Simian) -> None:
        return obj.walking()

class BeHuman:
    def be(self , obj : Human) -> None:
        return obj.speaking()


def main() -> None:
    simian = BeSimian()
    simian.be(Monkey())
    simian.be(Jaeyong())

    human = BeHuman()
    human.be(Jaeyong())
    human.be(Monkey())
    

if __name__ == '__main__':
    main()