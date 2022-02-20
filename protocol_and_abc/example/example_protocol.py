from typing import Protocol


class Human(Protocol):
    def speaking(self) -> None:
        ...
    
    def walking(self) -> None:
        ...

class Simian(Protocol):
    def walking(self) -> None:
        ...


class Jaeyong():
    def speaking(self) -> None:
        print(
            f"{type(self)} is speaking" 
            )
    def walking(self) -> None:
        print(
            f"{type(self)} is walking" 
            )

class Monkey():
    def walking(self) -> None:
        print(
            f"{type(self)} is walking" 
        )
    

class BeSimian:
    """사람도 원숭이도 유인원"""
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

if __name__ == '__main__' :
    main() 