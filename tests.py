from unittest import TestCase, main
from memgraph import Graph


class GraphTest(TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_size(self):
        self.graph[4,5] = 1
        assert self.graph.size == 20

    def test_search(self):
        self.graph[1,2] = 1
        self.graph[2,4] = 1
        assert list(self.graph.search(1)) == [(1,2), (2,4)]

    def test_getitem(self):
        self.graph[1,2] = 8
        assert self.graph[1,2] == 8
        assert self.graph[1,3] is None

        self.graph[1,2] = 2
        self.graph[1,3] = 2
        assert self.graph[1] == {2: 2, 3: 2}

    def test_delitem(self):
        self.graph[1,2] = 8
        self.graph[1,3] = 9
        del self.graph[1,2]
        assert not self.graph[1,2]

        del self.graph[1]
        assert not self.graph[1]


if __name__ == '__main__':
    main()
