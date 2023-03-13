from abc import ABCMeta
from typing import Union


class IPerson(metaclass=ABCMeta):

    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age

    def get(self):
        raise NotImplementedError("Abstract method invocation")


class Student(IPerson):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def get(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def get(self):
        print("I am a teacher")


# Dependency Injection is better than Factory Pattern
class PersonFactory:

    @staticmethod
    def build_person(person_type: str) -> Union[Student, Teacher]:
        if person_type == "student":
            return Student("hashim", 21)
        elif person_type == "teacher":
            return Teacher("haroon", 45)
        else:
            raise ValueError("Invalid type passed to factory")


def main():
    # Factory client code
    choice = input()
    person = PersonFactory().build_person(choice)
    person.get()


if __name__ == '__main__':
    main()
