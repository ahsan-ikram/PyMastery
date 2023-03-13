class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter in pythonic way
    @property
    def name(self):
        return self.__name

    # Setter in pythonic way
    @name.setter
    def name(self, name):
        self.__name = name

    # Getter in pythonic way
    @property
    def age(self):
        return self.__age

    # Setter in pythonic way
    @age.setter
    def age(self, age):
        self.__age = age

    @staticmethod
    def class_function():
        print("Static method is invoked")

    def __repr__(self):
        return f"Person Name = {self.__name} Age = {self.__age}"


def main():
    p1 = Person("Alex", 21)
    print(p1.name)
    print(p1.age)
    Person.class_function()
    p1.class_function()


if __name__ == "__main__":
    main()
