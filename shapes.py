def square(width: int = 10) -> None:
    for _ in range(width):
        for _ in range(width):
            print('*', sep='', end='')
        print('', sep='')


# TODO: add orientation parameter to the function
def right_triangle(width: int = 10) -> None:
    for i in range(width):
        for j in range(width):
            if j <= i:
                print('*', sep='', end='')
        print('', sep='')


def diamond(width: int = 10) -> None:
    raise NotImplementedError('Wait for it')


def main():
    diamond()


if __name__ == '__main__':
    main()
