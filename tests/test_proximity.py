from grl.proximity import within, proximity, diamond_proximity


origin = (0, 0)


def test_within():
    assert within((1, 0), 1, of=origin)
    assert within((1, 0), 2, of=(2, 0))

    assert not within((1, 0), 0, of=origin)
    assert not within((2, 0), 1, of=origin)


def test_proximity():
    assert set(proximity(1, origin)) == set([
        (-1,1), (0,1), (1,1),
        (-1,0), (0,0), (1,0),
        (-1,-1),(0,-1),(1,-1),
        ])


def test_diamond_proximity():
    assert set(diamond_proximity(2, origin)) == set([
        (0,2),
        (-1,1), (0,1), (1,1),
        (-2,0), (-1,0), (0,0), (1,0), (2,0),
        (-1,-1),(0,-1),(1,-1),
        (0,-2),
    ])
