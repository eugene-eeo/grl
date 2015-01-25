from collections import namedtuple
from itertools import islice, count


Point = namedtuple('Point', ('x', 'y'))


def slicerange(values, sl):
    if not values:
        return
    it = islice(
        count(sl.start or 0),
        sl.start,
        sl.stop,
        sl.step,
    )
    maxvalue = max(values)
    for item in it:
        if item in values:
            yield item
        if item >= maxvalue:
            return


class View(object):
    def __init__(self, graph, slices):
        self.graph = graph
        self.sx, self.sy = slices
        self.delta = Point(
            x=self.sx.start or 0,
            y=self.sy.start or 0,
        )

    @property
    def board(self):
        return self.graph.board

    def relative(self, coordinate):
        x, y = coordinate
        dx, dy = self.delta
        return (x + dx), (y + dy)

    def __getitem__(self, coordinate):
        if isinstance(coordinate, int):
            x = coordinate + self.delta.x
            return self.graph[x]
        return self.graph[self.relative(coordinate)]

    def __delitem__(self, coordinate):
        if isinstance(coordinate, int):
            x = coordinate + self.delta.x
            del self.graph[x]
            return
        del self.graph[self.relative(coordinate)]

    def __setitem__(self, coordinate, value):
        self.graph[self.relative(coordinate)] = value

    def __iter__(self):
        board = self.board
        for x in slicerange(board, self.sx):
            for y in slicerange(self.board[x], self.sy):
                yield x, y

    def values(self):
        for coordinate in self:
            yield self[coordinate]
