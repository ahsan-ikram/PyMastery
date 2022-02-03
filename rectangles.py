from dataclasses import dataclass


# Problem
# Given a 2D dimensional space
# A set point of given in 2D space
# Count the number of rectangles
# Example

# (0,0), (0,1), (1,0), (1,1) -> 1
# (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) -> 9
# (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2), (2,3) -> 9

@dataclass
class Point:
    x: int
    y: int


def main():
    pass


if __name__ == '__main__':
    main()
