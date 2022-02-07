"""
Intent
    State is a behavioral design pattern that lets an object alter its behavior when its
    internal state changes.
    It appears as if the object changed its class.

Example
    Buttons of the smartphone behave differently depending on the state

Pros

    Single Responsibility Principle. Organize the code related to particular states into separate classes.
    Open/Closed Principle. Introduce new states without changing existing state classes or the context.
    Simplify the code of the context by eliminating bulky state machine conditionals.

 Cons
    Applying the pattern can be overkill if a state machine has only a few states or rarely changes.

"""

from abc import abstractmethod


class State:
    @abstractmethod
    def say_hi(self):
        pass

    @abstractmethod
    def say_bye(self):
        pass


class Happy(State):
    def say_hi(self):
        return 'Hey! How are you doing bro!'

    def say_bye(self):
        return 'See you soon bro!'


class Sad(State):
    def say_hi(self):
        return 'Hi!'

    def say_bye(self):
        return 'Bye! I am going to cry'


class Person:
    def __init__(self, state: State):
        self._state = state

    def update_state(self, new_state: State):
        self._state = new_state

    def say_hi(self):
        return self._state.say_hi()

    def say_bye(self):
        return self._state.say_bye()


def main():
    person = Person(Happy())

    print(person.say_hi())
    print(person.say_bye())
    person.update_state(Sad())
    print(person.say_hi())
    print(person.say_bye())


if __name__ == '__main__':
    main()
