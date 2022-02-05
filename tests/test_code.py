import pytest
import typing
from utils.vertex import Vertex
from challenge.rectangles import count_rectangles


@pytest.fixture
def get_square() -> typing.List[Vertex]:
    return [Vertex(0, 0), Vertex(0, 1), Vertex(1, 0), Vertex(1, 1)]


@pytest.fixture
def get_rectangle() -> typing.List[Vertex]:
    return [Vertex(0, 0), Vertex(0, 2), Vertex(1, 0), Vertex(1, 2)]


def test_count_rectangles(get_square):
    assert count_rectangles(get_square) == 1
