import string

"""
Generator is type of Iterator
Generator -> Functions that act like Iterators
Generator -> Generates elements in a look
Generator -> On demand iteration
Iterators -> Loops over objects in memory
"""


def f():
    return 1
    return 2
    return 3


print(f"f() return {f()}")


def g():
    """ Analogy of ping pong opponent which returns the serve until yields are exhausted"""
    yield 1
    yield 3
    yield 3


result = g()
print(f"g() return {result}")

for i in result:
    print(i)


def letters():
    for c in string.ascii_lowercase:
        yield c


# Generates letter during each loop iteration
for letter in letters():
    print(letter)
