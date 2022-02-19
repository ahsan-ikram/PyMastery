def f_with_yield():
    """Return a generator -> iterable object"""
    yield 1
    yield 2
    yield 3


def f_with_return():
    return 1
    return 2
    return 3


def main():
    print(f_with_return())
    print([x for x in f_with_yield()])


if __name__ == '__main__':
    main()
