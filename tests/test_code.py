import pytest
import typing
from utils.vertex import Vertex
from challenge.rectangles import count_rectangles


@pytest.fixture
def square_vertices() -> typing.List[Vertex]:
    return [Vertex(0, 0), Vertex(0, 1), Vertex(1, 0), Vertex(1, 1)]


@pytest.fixture
def rectangle_vertices() -> typing.List[Vertex]:
    return [Vertex(0, 0), Vertex(0, 2), Vertex(1, 0), Vertex(1, 2)]


def test_non_polygon():
    assert count_rectangles(None) == 0
    assert count_rectangles([]) == 0
    assert count_rectangles([Vertex(0, 0)]) == 0
    assert count_rectangles([Vertex(0, 0), Vertex(0, 0)]) == 0
    assert count_rectangles([Vertex(0, 0), Vertex(0, 1), Vertex(1, 0)]) == 0


def test_count_rectangles(square_vertices):
    assert count_rectangles(square_vertices) == 1
