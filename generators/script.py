from memory_profiler import profile

N = 1000000


def square_generator():
    """ Infinite square generator """
    x = 0
    while True:
        yield x * x
        x += 1


@profile
def data_without_generator():
    sequence = [x * x for x in range(1, N)]
    return sequence


@profile
def data_with_generator():
    generator = square_generator()
    return generator


@profile
def process_data(buffer):
    for index, value in enumerate(buffer):
        if index >= N:
            break


@profile
def main():
    process_data(data_without_generator())
    process_data(data_with_generator())


if __name__ == '__main__':
    main()
