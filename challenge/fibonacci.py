import time


# Fibonacci Numbers
# f(x) = f(x-1) + f(x-2)
# where x is integer and x >= 0
# f(0) = 0 and f(1) = 1

def recursive_fib(index: int) -> int:
    if int(index) < 0:
        raise ValueError("index must be > 0")
    if index in [0, 1]:
        return index
    return recursive_fib(index - 1) + recursive_fib(index - 2)


def iterative_fib(index: int) -> int:
    if index in [0, 1]:
        return index
    else:
        previous, current = 0, 1
        for _ in range(index - 1):
            previous, current = current, previous + current
    return current


def main():
    start = time.perf_counter()
    print(f'iterative_fib(10) = {iterative_fib(15)}')
    end = time.perf_counter()
    print(f'Iterative approach time = {end - start} seconds')

    start = time.perf_counter()
    print(f'recursive_fib(10) = {recursive_fib(15)}')
    end = time.perf_counter()
    print(f'Recursive approach time = {end - start} seconds')


if __name__ == '__main__':
    main()
