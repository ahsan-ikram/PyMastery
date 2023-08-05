def cube(x): return x ** 3


def main():
    numbers = [1, 2, 3, 4, 5]
    # pep-8 does not allow this
    cube = lambda x: x ** 3  # NOQA
    print(cube(2))

    # Anonymous function itself (without being invoked)
    print(lambda x: (x ** 2)(5))

    # Anonymous function can be invoked like this
    print((lambda x: x ** 2)(5))

    # Transformation operation
    print(list(map(lambda x: x ** 2, numbers)))
    # Transformation + Summation
    print(sum(map(lambda x: x ** 2, numbers)))

    # Lambda for filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

    # Map + Reduce Operation
    from functools import reduce
    print(reduce(lambda x, y: x + y, [1]))


if __name__ == '__main__':
    main()

