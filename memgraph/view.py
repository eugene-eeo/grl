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

    @property
    def board(self):
        return self.graph.board

    @property
    def relative_delta(self):
        return Point(
            x=self.sx.start or 0,
            y=self.sy.start or 0,
        )

    def relative_point(self, coordinate):
        x, y = coordinate
        delta = self.relative_delta
        return (x + delta.x), (y + delta.y)

    def __getitem__(self, coordinate):
        if isinstance(coordinate, int):
            x = coordinate + self.relative_delta.x
            return self.graph[x]
        t = self.relative_point(coordinate)
        return self.graph[t]

    def __delitem__(self, coordinate):
        if isinstance(coordinate, int):
            x = coordinate + self.relative_delta.x
            del self.graph[x]
            return
        t = self.relative_point(coordinate)
        del self.graph[t]

    def __setitem__(self, coordinate, value):
        self.graph[self.relative_point(coordinate)] = value

    def __iter__(self):
        board = self.board
        for x in slicerange(board, self.sx):
            y_axis = board[x]
            for y in slicerange(y_axis, self.sy):
                yield x, y

    def values(self):
        for coordinate in self:
            yield self[coordinate]
