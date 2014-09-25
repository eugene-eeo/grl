from memgraph.utils import proximity, diagonal, diamond_proximity, distance


def test_proximity():
    start = (0,0)
    it = list(proximity(1, start))
    for x, y in it:
        assert -1 <= x <= 1
        assert -1 <= y <= 1
    assert len(it) == 9


def test_diagonal():
    it = list(diagonal(3, (0,0), 1))
    assert it == [
        (0, 0),
        (1, 1),
        (2, 2),
    ]


def test_diamond_proximity():
    start = (0,0)
    it = set(diamond_proximity(1, start))
    assert it == set([
        (0, -1),
        (-1, 0),
        (0, 0),
        (1, 0),
        (0, 1),
    ])


def test_distance():
    assert distance((0,0), (3,4)) == 5
    assert distance((0,0), (0,0)) == 0
