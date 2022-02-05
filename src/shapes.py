def square(width: int = 10) -> None:
    for _ in range(width):
        for _ in range(width):
            print('*', sep='', end='')
        print('', sep='')


def right_triangle(width: int = 10, left_orient: bool = True) -> None:
    if left_orient:
        for i in range(width):
            for j in range(width):
                if j <= i:
                    print('*', sep='', end='')
            print('', sep='')
    else:
        for i in reversed(range(width)):
            for j in range(width):
                if j >= i:
                    print('*', sep='', end='')
                else:
                    print(' ', sep='', end='')
            print('', sep='')


def triangle(width: int = 11) -> None:
    center = int(width / 2)
    for i in range(center):
        for j in range(width):
            if center - i <= j <= center + i:
                print('*', sep='', end='')
            else:
                print(' ', sep='', end='')
        print('', sep='')


def diamond(width: int = 11) -> None:
    center = int(width / 2)
    for i in range(width):
        for j in range(width):
            if i <= center:
                if center - i <= j <= center + i:
                    print('*', sep='', end='')
                else:
                    print(' ', sep='', end='')
            else:
                if i - center <= j <= center + width - i - 1:
                    print('*', sep='', end='')
                else:
                    print(' ', sep='', end='')
        print('', sep='')


def main():
    square()
    right_triangle()
    right_triangle(left_orient=False)
    triangle()
    diamond()


if __name__ == '__main__':
    main()
