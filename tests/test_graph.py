def test_setitem(graph):
    graph[1,2] = 1
    assert graph.board[1][2] == 1


def test_delitem(graph):
    graph[1,2] = 1
    del graph[1,2]
    assert not graph[1,2]

    graph[1,3] = 2
    graph[1,4] = 3
    del graph[1]
    assert not graph[1]


def test_getitem(graph):
    graph[1,2] = 1
    graph[1,3] = 2

    assert graph[1,2] == 1
    assert graph[1] == {2: 1, 3: 2}


def test_search(graph):
    graph[1,1] = 1
    assert list(graph.search(1)) == [(1,1)]


def test_size(graph):
    graph[4,5] = 1
    assert graph.size == 20
