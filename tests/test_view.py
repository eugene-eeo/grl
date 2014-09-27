def test_view_iter(graph):
    for item in range(0, 3):
        graph[0,item] = item

    view = graph.view[:, 0:3]
    assert list(view) == [(0,0), (0,1), (0,2)]


def test_view_items(graph):
    view = graph.view[1:, 0:3]
    view[0,0] = 1
    view[3,3] = 2

    assert graph[1,0] == view[0,0] == 1
    assert graph[4,3] == view[3,3] == 2

    del view[0,0]
    del view[3,3]

    assert not graph[1,0]
    assert not graph[4,3]


def test_view_range(graph):
    view = graph.view[1:, 0:3]
    graph[5,5] = 1
    graph[5,6] = 2

    assert not list(view.values())
