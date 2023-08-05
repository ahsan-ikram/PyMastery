def cube(x): return x ** 3


def main():
    # pep-8 does not allow this
    cube = lambda x: x ** 3  # NOQA
    print(cube(2))

    # Anonymous function itself (without being invoked)
    print(lambda x: (x ** 2)(5))

    # Anonymous function can be invoked like this
    print((lambda x: x ** 2)(5))

    print(list(map(lambda x: x ** 2, [1, 2, 3])))

    print(sum(map(lambda x: x ** 2, [1, 2, 3])))


if __name__ == '__main__':
    main()

