import typing
from utils.vertex import Vertex


# Problem
# Given a 2D dimensional space
# A set point of given in 2D space
# Count the number of rectangles
# Example

# (0,0), (0,1), (1,0), (1,1) -> 1
# (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) -> 9
# (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2), (2,3) -> 9

def count_rectangles(vertices: typing.List[Vertex]):
    if vertices is None or len(vertices) < 4:
        return 0
    # Implement the Logic
    for vertex in vertices:
        x,y = vertex

    return -1


def main():
    mydict = {'2': 'b', '1': 'a'}
    print(mydict)
    print(f'Rectangles detected = {count_rectangles([])}')


if __name__ == '__main__':
    main()
