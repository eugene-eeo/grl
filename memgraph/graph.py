from collections import defaultdict
from functools import partial
from operator import eq
from memgraph.view import View


def default_null():
    return


class Graph(object):
    def __init__(self, null=default_null):
        self.board = defaultdict(lambda: defaultdict(null))

    def __getitem__(self, point):
        if isinstance(point, int):
            return self.board[point]
        x, y = point
        return self.board[x][y]

    def __setitem__(self, point, value):
        x, y = point
        self.board[x][y] = value

    def __delitem__(self, point):
        if isinstance(point, int):
            del self.board[point]
            return
        x, y = point
        del self.board[x][y]

    def __iter__(self):
        for x in sorted(self.board):
            for y in sorted(self.board[x]):
                yield x, y

    def __contains__(self, point):
        x, y = point
        return x in self.board and y in self.board[x]

    def values(self):
        for t in self:
            yield self[t]

    def filter(self, function):
        for t in self:
            if function(self[t]):
                yield t

    def search(self, value):
        return self.filter(partial(eq, value))

    @property
    def size(self):
        max_x = max(self.board)
        max_y = 0
        for column in self.board.values():
            if column:
                max_y = max(max_y, max(column))
        return max_x * max_y

    @property
    def view(self):
        class ViewBuilder(object):
            def __getitem__(ins, slices):
                return View(self, slices)
        return ViewBuilder()
