from pytest import fixture
from memgraph import Graph


@fixture
def graph():
    return Graph()
