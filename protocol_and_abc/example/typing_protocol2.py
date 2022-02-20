'''
Python Type Hints - Duck typing with Protocol

reference :https://andrewbrookins.com/technology/building-implicit-interfaces-in-python-with-protocol-classes/

'''

from typing import Protocol

class Flyer(Protocol):
        def fly(self) -> None:
            """Flyer can fly"""
class FlyingHero:
    """This hero can fly """
    def fly(self):
        """flying:)"""
        print(f"{type(self)} is flying ")

class RunningHero:
    """this hero only run """
    def running(self):
        """run run run"""
        print(f"{type(self)} is Running ")

class Board:
    """An imaginary game board that doesn't do anything """
    def make_fly(self , obj : Flyer) -> None:
        return obj.fly()


def main()-> None:
    board = Board()
    board.make_fly(FlyingHero())
    board.make_fly(RunningHero())

if __name__ == '__main__':
    main()
