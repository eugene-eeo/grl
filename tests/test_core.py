from grl.core import boundaries, cycle, diagonal, distance


origin = (0, 0)


def test_boundaries():
    assert boundaries(0, origin) == (0, 0, 0, 0)
    assert boundaries(2, origin) == (-2, 2, -2, 2)


def test_cycle():
    assert list(cycle(0)) == [0]
    assert list(cycle(1)) == [0, 1, 0]
    assert list(cycle(2)) == [0, 1, 2, 1, 0]


def test_diagonal():
    assert list(diagonal(0, origin, 0)) == []
    assert list(diagonal(1, origin, 1)) == [(1, 1)]
    assert list(diagonal(2, origin, 2)) == [(1, 2), (2, 4)]


def test_distance():
    assert distance(origin, origin) == 0
    assert distance(origin, (3, 4)) == 5
