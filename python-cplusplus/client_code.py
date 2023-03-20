import time
import cv2
from build.module_name import *

from concurrent.futures import ThreadPoolExecutor


def call_function_from_c():
    arg1 = 10
    arg2 = 20
    print(f"C/C++ function returns = {process_in_c(arg1, arg2)}")  # noqa


def call_class_function_in_c():
    print(f"Class in C/C++ is available as {PyCClass}")  # noqa
    m = get_c_class(10)  # noqa
    m2 = PyCClass(10)  # noqa
    print(f"Object 1 = {m} Object 2 = {m2}")
    print(f"C/C++ class method return = {m.multiply(20)}")


def main():
    print("Experimenting with C/C++ function")
    print("----------------------------------------------------------")
    call_function_from_c()

    print("\n\nExperimenting with C/C++ Class")
    print("----------------------------------------------------------")
    call_class_function_in_c()


if __name__ == '__main__':
    main()


def array_processing_in_c():
    m = get_c_class(10)  # noqa
    arr = m.multiply_list([0.0, 1.0, 2.0, 3.0])
    print(arr)
    print(m.multiply_two(50, 200))
    print(m.image)
    print(m.image.shape)
    cv2.imwrite("/tmp/test.png", m.image)
    print(m.multiplier)
    m.multiplier = 100
    print(m.multiplier)
    start = time.time()
    with ThreadPoolExecutor(4) as ex:
        ex.map(lambda x: m.function_that_takes_a_while(), [None] * 4)
    print(f"Threaded fun took {time.time() - start} seconds")
