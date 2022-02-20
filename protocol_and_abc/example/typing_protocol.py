'''
Python Type Hints - Duck typing with Protocol

reference :https://adamj.eu/tech/2021/05/18/python-type-hints-duck-typing-with-protocol/

usually python is known duck typing langauge 
but  the typing(checking types) seems at odds with duck typing
because it restricts variables to named types(classes) , allowing only types.

'''
class Duck:
    def quack(self) -> str:
        return "Quack"

def sonorize(duck : Duck) -> None:
    print(duck.quack)

sonorize(Duck())

'''
using typing - protocol
'''
from typing import Protocol

class Quacker(Protocol):
    def quack(self) -> str:
        pass

class Duck2:
    def quack(self) -> str:
        return "Quack"

class MegaDuck:
    def quack(self) -> str:
        return "QuackQuack"

def sonorize2(duck2 :Quacker) -> None:
    print(duck2.quack())

sonorize2(Duck())
sonorize2(MegaDuck())

