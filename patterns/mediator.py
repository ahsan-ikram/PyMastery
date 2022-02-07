"""
Mediator Design Pattern
    Mediator is a behavioral design pattern.
    Reduces coupling between components of a program by making them communicate indirectly,
    through a special mediator object.
Example
    Aircraft pilots don’t talk to each other directly when deciding who gets to land their plane next.
    All communication goes through the control tower.

Pros
    Single Responsibility Principle.
    You can extract the communications between various components into a single place, making it
    easier to comprehend and maintain.
    Open/Closed Principle. You can introduce new mediators without having to change the actual components.
    You can reduce coupling between various components of a program.
    You can reuse individual components more easily.

Cons
    Over time a mediator can evolve into a God Object.


"""

from abc import ABC, abstractmethod


class AirTrafficController(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass


class Airline:
    def __init__(self, mediator: AirTrafficController = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> AirTrafficController:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: AirTrafficController) -> None:
        self._mediator = mediator


class Emirates(Airline):
    def do_a(self) -> None:
        print("Emirates does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Emirates does B.")
        self.mediator.notify(self, "B")


class AirFrance(Airline):
    def do_c(self) -> None:
        print("AirFrance does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("AirFrance does D.")
        self.mediator.notify(self, "D")


class BerlinTower(AirTrafficController):
    def __init__(self, emirates: Emirates, air_france: AirFrance) -> None:
        self._emirates = emirates
        self._emirates.mediator = self
        self._air_france = air_france
        self._air_france.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("BerlinTower reacts on A and triggers following operations:")
            self._air_france.do_c()
        elif event == "D":
            print("BerlinTower reacts on D and triggers following operations:")
            self._emirates.do_b()
            self._air_france.do_c()


def main():
    c1 = Emirates()
    c2 = AirFrance()
    BerlinTower(c1, c2)
    c1.do_a()
    print("\n", end="")
    c2.do_d()


if __name__ == '__main__':
    main()
