from operator import eq
from functools import partial
from collections import defaultdict


def default_null():
    return


class Graph(object):
    def __init__(self, null=default_null):
        self.board = defaultdict(lambda: defaultdict(null))

    def __getitem__(self, coordinate):
        if isinstance(coordinate, int):
            return self.board[coordinate]
        x, y = coordinate
        return self.board[x][y]

    def __setitem__(self, coordinate, value):
        x, y = coordinate
        self.board[x][y] = value

    def __delitem__(self, coordinate):
        if isinstance(coordinate, int):
            del self.board[coordinate]
            return
        x, y = coordinate
        del self.board[x][y]

    def __iter__(self):
        for x in self.board:
            for y in self.board[x]:
                yield x, y

    def filter(self, function):
        for x, y in self:
            if function(self[x, y]):
                yield x, y

    def search(self, value):
        return self.filter(partial(eq, value))

    @property
    def size(self):
        max_x = max(self.board)
        max_y = 0
        for column in self.board.values():
            if not column:
                continue
            length = max(column)
            if length > max_y:
                max_y = length
        return max_x * max_y

    def values_of(self, iterable):
        for x, y in iterable:
            yield self[x, y]
