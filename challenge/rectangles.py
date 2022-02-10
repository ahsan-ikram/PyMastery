import typing
from itertools import combinations
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
    # Consider 2D plane with x-axis on horizontal line and y-axis at vertical lines
# BUGGY
    vindex = {}
    hindex = {}
    for v in vertices:
        vindex.setdefault(v.x, []).append(v.y)
        hindex.setdefault(v.y, []).append(v.x)
    for _, y in vindex.items():
        comb = list(combinations(y, 2))
        count = 0
        for i in comb:
            if i in hindex.keys():
                count += 1

    result = count if count % 2 == 0 else count - 1
    return result


def main():
    mydict = {'2': 'b', '1': 'a'}
    print(mydict)
    print(f'Rectangles detected = {count_rectangles([])}')


if __name__ == '__main__':
    main()
