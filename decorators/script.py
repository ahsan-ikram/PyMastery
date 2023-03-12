def my_decorator(function):
    def wrapper(*args, **kwargs):
        """ Any function signature is now supported """
        print("Python function is being decorated")
        return function(*args, **kwargs)

    return wrapper


@my_decorator
def add(x, y):
    return x + y


def main():
    print(add(1, 2))


if __name__ == '__main__':
    main()
