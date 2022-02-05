from src import other


# Challenge No. 1
# Given a n digit number is equal to sum to individual digits raise to the power total digits
# Example

# 2 = pow(2,1)
# 10 != pow(1,2) + pow(0,2)

# X1X2X3 = X1**3 + X2**3 + X3**3

def check(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    return n == sum([pow(int(digit), power) for digit in digits])


def myfunction(arg: str):
    print(f'arg object from myfunction = {arg} with id = {hex(id(arg))}')
    arg.capitalize()
    print(f'arg object from myfunction = {arg} with id = {hex(id(arg))}')


def main():
    print(f'app.py module = {__name__} {hex(id(__name__))}')
    other.display_builtin_name()
    print(f'app.py module = {__name__} {hex(id(__name__))}')


if __name__ == '__main__':
    main()
