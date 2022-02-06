class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


class SingletonWithBorg(Borg):
    pass


if __name__ == '__main__':
    obj1 = SingletonWithBorg()
    obj2 = SingletonWithBorg()

    obj1.name = 'Obj1'
    obj2.name = 'Obj2'

    print(obj1.name)
